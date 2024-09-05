import os
import argparse
import json
import time
import torch
import torch.nn as nn
from torch.optim.lr_scheduler import ReduceLROnPlateau
from torch.utils.data import DataLoader
import pytorch_lightning as pl
from pytorch_lightning.callbacks import ModelCheckpoint, EarlyStopping
from look2hear.utils.parser_utils import prepare_parser_from_dict, parse_args_as_dict
import look2hear.models
import look2hear.videomodels
import yaml
from ptflops import get_model_complexity_info
from rich import print

def check_parameters(net):
    """
        Returns module parameters. Mb
    """
    parameters = sum(param.numel() for param in net.parameters())
    return parameters / 10 ** 6


def flops_selective_scan_fn(B=1, L=256, D=768, N=16, with_D=True, with_Z=False, with_Group=True, with_complex=False):
    """
    u: r(B D L)
    delta: r(B D L)
    A: r(D N)
    B: r(B N L)
    C: r(B N L)
    D: r(D)
    z: r(B D L)
    delta_bias: r(D), fp32
    
    ignores:
        [.float(), +, .softplus, .shape, new_zeros, repeat, stack, to(dtype), silu] 
    """
    assert not with_complex 
    # https://github.com/state-spaces/mamba/issues/110
    flops = 9 * B * L * D * N
    if with_D:
        flops += B * D * L
    if with_Z:
        flops += B * D * L    
    return flops

def selective_scan_flop_jit():
    B, D, L = 126, 512, 250
    N = 16
    flops = flops_selective_scan_fn(B=B, L=L, D=D, N=N, with_D=True, with_Z=True, with_Group=True)
    return flops

parser = argparse.ArgumentParser()
parser.add_argument(
    "--exp_dir", default="exp/tmp", help="Full path to save best validation model"
)

with open("configs/tfgnet.yml") as f:
    def_conf = yaml.safe_load(f)
parser = prepare_parser_from_dict(def_conf, parser=parser)

arg_dic, plain_args = parse_args_as_dict(parser, return_plain_args=True)
audiomodel = getattr(look2hear.models, arg_dic["audionet"]["audionet_name"])(
    sample_rate=arg_dic["datamodule"]["data_config"]["sample_rate"],
    **arg_dic["audionet"]["audionet_config"]
)

with torch.cuda.device(3):
    a = torch.randn(1, 1, 16000).cuda()
    total_macs = 0
    total_params = 0
    # DPRNN
    model = audiomodel.cuda()
    with torch.no_grad():
        macs, params = get_model_complexity_info(
            model, (16000,), as_strings=False, print_per_layer_stat=True, verbose=False
        )
    # print(model(a).shape)
    total_macs += macs

    # selective_scan
    macs = selective_scan_flop_jit() * 24 
    
    total_macs += macs

    # in_proj
    macs = 24 * 120 * 10 ** 6 
    
    total_macs += macs

    # dt_proj
    macs = 24 * 4.12 * 10 ** 9
    
    total_macs += macs
    total_params += params
    print("MACs: ", total_macs / 10.0 ** 9)
    print("Params: ", total_params / 10.0 ** 6)
    # for i in range(1000):
    #     model(a)
