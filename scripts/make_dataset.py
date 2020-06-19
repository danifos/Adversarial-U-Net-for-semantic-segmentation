import numpy as np
import cv2 as cv
import os
import os.path as osp

in_dir = 'dataset'
out_dir = 'paired_dataset'

pairs_dir = [['train', 'new train set/train_img', 'new train set/train_label'],
             ['test', 'new_test_set/test_img', 'new_test_set/test_label']]

os.mkdir(out_dir)

for out_split, in_img, in_label in pairs_dir:
    img_dir = osp.join(in_dir, in_img)
    label_dir = osp.join(in_dir, in_label)
    pair_dir = osp.join(out_dir, out_split)

    os.mkdir(pair_dir)

    for f in list(os.walk(img_dir))[0][2]:
        img = cv.imread(osp.join(img_dir, f))
        label = cv.imread(osp.join(label_dir, f))
        pair = np.concatenate((img, label), 1)
        cv.imwrite(osp.join(pair_dir, f), pair)
