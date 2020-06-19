# Adversarial U-Net in PyTorch

Training and testing Adversarial U-Net, as well as experimenting the objective function.

## Dependencies
- Python 3.6
- PyTorch 0.4 and CUDA CuDNN
- Other packages that can be installed by `pip install -r requirements.txt`

## Usage

Basically, you can train and test the model by:
```sh
python train.py --dataroot ../paired_dataset/ --name $dir_name --n_epochs 400 --n_epochs_decay 200 --model pix2pix --direction AtoB --input_nc 1 --output_nc 1
python test.py --dataroot ../paired_dataset/ --name $dir_name --model pix2pix --direction AtoB --input_nc 1 --output_nc 1
```
Options of the scripts can be found in `options/` and `model/pix2pix.py`.

If you want to test different configurations in batch, run the Shell scripts in `experiments/`. The experiment results will be listed in `experiment_*.log`.
