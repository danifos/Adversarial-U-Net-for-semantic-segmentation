from __future__ import division, print_function
import numpy as np
import cv2 as cv
import argparse
import os
import matplotlib.pyplot as plt


def remove_ticks():
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)


def main():
    assert(len(args.images) == len(args.labels))
    num_images = len(args.images)

    size = None
    tptn = 0
    fpfn = 0
    total = 0
    for i, (image, label) in enumerate(zip(args.images, args.labels)):
        image = cv.imread(image)
        label = cv.imread(label)
        assert image.dtype == np.uint8 and label.dtype == np.uint8
        image = image / 255
        label = label / 255
        if len(image.shape) == 3:
            image = image[..., 0]
        if len(label.shape) == 3:
            label = label[..., 0]
        if size is None:
            size = label.shape
        else:
            assert size == label.shape
        image = cv.resize(image, (size[1], size[0]))
        _, image = cv.threshold(image, 0.5, 1, cv.THRESH_BINARY)
        _, label = cv.threshold(label, 0.5, 1, cv.THRESH_BINARY)

        tptn += (image == label).sum()
        fpfn += (image != label).sum()
        total += size[0] * size[1]

        if args.visualize:
            plt.subplot(2, num_images, i+1)
            plt.imshow(image, cmap='gray')
            remove_ticks()
            plt.subplot(2, num_images, num_images+i+1)
            plt.imshow(label, cmap='gray')
            remove_ticks()

    assert tptn+fpfn == total
    print('acc:', tptn / (tptn+fpfn))

    if args.visualize:
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--images', nargs='+', type=str)
    parser.add_argument('-l', '--labels', nargs='+', type=str)
    parser.add_argument('-t', '--threshold', type=float, default=0.5)
    parser.add_argument('-v', '--visualize', action='store_true')
    args = parser.parse_args()
    main()
