import numpy as np
import cv2 as cv
import argparse
import os


def main():
    size = None
    tptn = 0
    fpfn = 0
    for image, label in zip(args.images, args.labels):
        image = cv.imread(image)
        label = cv.imread(label)
        if len(image.shape) == 3:
            image = image[..., 0]
        if len(label.shape) == 3:
            label = label[..., 0]
        if size is None:
            size = label.shape
        else:
            assert size == label.shape
        image = cv.resize(image,(size[1], size[0]))
        _, image = cv.threshold(image, 0.5, 1, cv.THRESH_BINARY)
        _, label = cv.threshold(label, 0.5, 1, cv.THRESH_BINARY)
        tptn = (image == label).sum()
        fpfn = (image != label).sum()
    print('acc:', tptn / (tptn+fpfn))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--images', nargs='+', type=str)
    parser.add_argument('-l', '--labels', nargs='+', type=str)
    parser.add_argument('-t', '--threshold', type=float, default=0.5)
    args = parser.parse_args()
    main()
