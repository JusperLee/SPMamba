# SPMamba: State-space model is all you need in speech separation

[![arXiv](https://img.shields.io/badge/arXiv-2404.02063-b31b1b.svg)](https://arxiv.org/abs/2404.02063)
[![GitHub Stars](https://img.shields.io/github/stars/JusperLee/SPMamba?style=social)](https://github.com/JusperLee/SPMamba/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9.16-blue.svg)](https://www.python.org/)

## 🔥 News

[2024-04-23] Update SPMamba MACs: **238.21 G/s** using [code](https://github.com/state-spaces/mamba/issues/110)

[2024-04-18] Update SPMamba **WSJ0-2Mix** Result


## Introduction

SPMamba revolutionizes the field of speech separation tasks by leveraging the power of Mamba in conjunction with the robust TF-GridNet infrastructure. By replacing the conventional bidirectional LSTM with a more efficient and effective bidirectional Mamba model, SPMamba sets a new standard for accuracy and performance in speech separation.

Built upon the open-source ESPnet framework, SPMamba offers a seamless experience for users looking to train their models with cutting-edge technology. Whether you're a researcher, developer, or enthusiast in the field of speech processing, SPMamba provides the tools and flexibility needed to achieve unparalleled results.

## Technology Stack

This repository is implemented using the ESPnet framework, a comprehensive platform for speech processing. SPMamba enhances ESPnet by integrating Mamba, a state-of-the-art state-space model, into the TF-GridNet architecture. This combination allows for significant improvements in speech separation tasks.

## Installation

clone the repository

```bash
git clone https://github.com/JusperLee/SPMamba.git && cd SPMamba
conda env create -f look2hear.yml
conda activate look2hear
```

## Usage

To train the SPMamba model, run the following command:

```bash
python audio_train.py --conf_dir=configs/spmamba.yml
```

## Performance

*Here, you can include a brief overview of the performance metrics or results that SPMamba achieves using own private datasets.*

| Model        | SDR  | SDRi | SI-SNR | SI-SNRi | Params(M) | Macs (G/s) |
|--------------|------|------|--------|---------|-----------|------------|
| Conv-TasNet  | 7.58 | 7.69 | 6.71   | 6.89    | 5.62      | 10.23      |
| DualPathRNN  | 5.76 | 5.87 | 4.88   | 5.06    | 2.72      | 85.32      |
| SudoRM-RF    | 7.59 | 7.70 | 6.66   | 6.84    | 2.72      | 4.60       |
| A-FRCNN      | 9.53 | 9.64 | 8.58   | 8.76    | 6.13      | 81.20      |
| TDANet       | 9.93 | 10.14| 8.95   | 9.21    | 2.33      | 9.13       |
| BSRNN        | 12.64| 12.75| 12.04  | 12.23   | 25.97     | 98.69      |
| TF-GridNet   | 13.59| 13.70| 12.62  | 12.81   | 14.43     | 445.56     |
| SPMamba   | 16.01| 16.14 | 15.20  | 15.33   | 6.14     | 238.21    |

## SPMamba in Self-built, WSJ0 and WHAM!

### Self-built

<img width="1125" alt="image" src="https://github.com/JusperLee/SPMamba/assets/33806018/8ee9767d-035a-412b-9432-2dcd7515703f">


### WSJ0

<img width="1130" alt="image" src="https://github.com/JusperLee/SPMamba/assets/33806018/754cdfbf-ccc9-46f5-a9b5-d9605a04dee4">


## License

SPMamba is licensed under the Apache License 2.0. For more details, see the [LICENSE](LICENSE) file in the repository.

## Acknowledgements

SPMamba is developed by the Look2Hear team at Tsinghua University. We would like to thank the ESPnet team for their contributions to the open-source community and for providing a solid foundation for our work.

## Citation

If you use SPMamba in your research or project, please cite the following paper:

```
@article{li2024spmamba,
  title={SPMamba: State-space model is all you need in speech separation},
  author={Li, Kai and Chen Guo},
  journal={arXiv preprint arXiv:2404.02063},
  year={2024}
}
```

## Contact

For any questions or feedback regarding SPMamba, feel free to reach out to us via email: tsinghua.kaili@gmail.com
