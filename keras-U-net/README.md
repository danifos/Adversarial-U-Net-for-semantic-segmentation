# Keras-U-net


## Model:


This deep neural network is implemented with Keras functional API, which makes it extremely easy to experiment with different interesting architectures.

Output from the network is a 256*256 which represents mask that should be learned. Sigmoid activation function makes sure that mask pixels are in [0, 1] range.


## Dependencies:


This model depends on the following libraries:

* Tensorflow
* Keras >= 1.0

Also, this code should be compatible with Python versions 2.7-3.5.

## How to run:

just run main.py

You will see the predicted results of test image in data/membrane/test



