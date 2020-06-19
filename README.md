# U-Net and Adversarial U-Net on ISBI 2012 dataset

This is the code for segmentation of neuronal structures using U-Net and Adversarial U-Net.

## Setup

Clone this repository:
```sh
git clone https://github.com/danifos/Adversarial-U-Net-for-semantic-segmentation
cd Adversarial-U-Net-for-semantic-segmentation
```

Place [`dataset.zip`](https://oc.sjtu.edu.cn/courses/18062/files/1108293/download?verifier=S9HUzw5Cb0aM6VEm82dvKiZEZID12K81devFuMNZ&wrap=1) under `Adversarial-U-Net-for-semantic-segmentation/` and then prepare the dataset:
```sh
unzip dataset.zip
bash scripts/make_dataset.py
```

The resulting files will look like this:
```txt
Adversarial-U-Net-for-semantic-segmentation/
├── dataset/
|   ├── new_test_set/
|   │   ├── test_img/
|   │   └── test_label/
|   └── new train set/
|       ├── train_img/
|       └── train_label/
├── paired_dataset/
|   ├── test/
|   └── train/
...
```

## Usage
For more details about installation and usage, please refer to the documents in the following three directories:

- `keras-U-Net/`
> Fine-tuning U-Net by tweaking learning rate, batch size, data augmentation, etc.
- `pytorch-U-Net/`
> Conducting ablation study on U-Net.
- `pytorch-Adversarial-U-Net/`
> Implementation and experiments of Adversarial U-Net.

## Evaluation

For evaluation of Pixel Accuracy, Jaccard Index and F1 Score, use `scripts/eval_metrics.py`. For example:
```sh
python scripts/eval_metrics.py --images results/* --labels dataset/new_test_set/test_label/[0-4].png -t 0.5
```

For evaluation of "Foreground-restricted Rand Scoring after border thinning" and "Foreground-restricted Information Theoretic Scoring after border thinning", first convert predictions to binary images of size 512x512. For example:
```sh
for * in results; do ffmpeg -i $i -vf scale=512:512 -y $i; done
python scripts/binarize.py results/*
```
Then run `scripts/eval_ibsi.bsh` in [Fiji](http://fiji.sc/).

## Acknowledgements
Our code is based on the following three repositories:
- [Implementation of deep learning framework -- Unet, using Keras](https://github.com/zhixuhao/unet)
- [Pytorch 0.41 implementation of the U-Net for image semantic segmentation + Dataloader for ISBI 2012 Challenge](https://github.com/Mastercorp/U-Net-Pytorch-0.4)
- [CycleGAN and pix2pix in PyTorch](https://github.com/junyanz/pytorch-cyclegan-and-pix2pix)
