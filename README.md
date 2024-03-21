
# SPMamba: State-space model is all you need in separation task

## Introduction

SPMamba revolutionizes the field of speech separation tasks by leveraging the power of Mamba in conjunction with the robust TF-GridNet infrastructure. By replacing the conventional bidirectional LSTM with a more efficient and effective bidirectional Mamba model, SPMamba sets a new standard for accuracy and performance in speech separation.

Built upon the open-source ESPnet framework, SPMamba offers a seamless experience for users looking to train their models with cutting-edge technology. Whether you're a researcher, developer, or enthusiast in the field of speech processing, SPMamba provides the tools and flexibility needed to achieve unparalleled results.

## Technology Stack

This repository is implemented using the ESPnet framework, a comprehensive platform for speech processing. SPMamba enhances ESPnet by integrating Mamba, a state-of-the-art state-space model, into the TF-GridNet architecture. This combination allows for significant improvements in speech separation tasks.

## Installation

To get started with SPMamba, you'll need to have ESPnet installed. Additionally, the Mamba environment is required to leverage the full capabilities of SPMamba. Follow these steps to set up your environment:

1. **Install ESPnet**: Follow the official [ESPnet installation guide](https://github.com/espnet/espnet#installation) to set up ESPnet on your system.

2. **Install Mamba**: After setting up ESPnet, install the Mamba environment by running the following command:

   ```bash
   pip install mamba
   ```

   For more detailed instructions on installing Mamba, please refer to the [Mamba documentation](https://github.com/state-spaces/mamba).

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
| SPMamba   | 16.01| 16.14 | 15.20  | 15.33   | 6.14     | 78.69    |

## License

SPMamba is licensed under the Apache License 2.0. For more details, see the [LICENSE](LICENSE) file in the repository.

## Contact

For any questions or feedback regarding SPMamba, feel free to reach out to us via email: tsinghua.kaili@gmail.com