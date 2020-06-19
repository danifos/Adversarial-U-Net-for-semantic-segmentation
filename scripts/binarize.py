import sys
import cv2 as cv
import numpy as np

for f in sys.argv[1:]:
    image = cv.imread(f)
    image = image / 255
    image = image[..., 0]
    _, image = cv.threshold(image, 0.5, 1, cv.THRESH_BINARY)
    image = (image * 255).astype(np.uint8)
    cv.imwrite('binary_'+f, image)
