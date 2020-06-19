# U-Net in PyTorch

Mainly for ablation study of U-Net.

## Dependencies
- Python 2.7
- PyTorch 0.4 and CUDA CuDNN
- scipy and sacred

## Usage

First, select which specific model to use by uncommenting one of the last 4 lines of `model.py`:
- `Unet = OUnet`: Original U-Net
- `Unet = DUnet`: U-Net without skip connections, equivalent to FCN
- `Unet = SDUnet`: Shallow FCN with half of the convolutional layers removed
- `Unet = LUnet`: MLP

Next, use the following commands to train and test a model (in directory `Orig_U-net_1/`, for example):
```sh
bash generate_json.sh config_train.json Orig_U-net_1
python main.py  # now training the model
bash generate_json.sh config_test.json Orig_U-net_1
python main.py  # now testing the model
```

Finally, run `eval_all.sh` to evaluate the Pixel Accuracy of all the results.
