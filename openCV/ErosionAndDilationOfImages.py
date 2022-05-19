"""
Morphological operations are a set of operations that process images based on shapes. They apply a
structuring element to an input image and generate an output image. The most basic morphological
operations are two: Erosion and Dilation

Basics of Erosion:
    1. Erodes away the boundaries of the foreground object
    2. Used to diminish the features of an image.

Working of erosion:
    1. A kernel(a matrix of odd size(3,5,7) is convolved with the image.
    2. A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels
       under the kernel are 1, otherwise, it is eroded (made to zero).
    3. Thus all the pixels near the boundary will be discarded depending upon the size of the kernel.
    4. So the thickness or size of the foreground object decreases or simply the white region decreases
       in the image.

Basics of dilation:
    1. Increases the object area
    2. Used to accentuate features

Working of dilation:
    1. A kernel(a matrix of odd size(3,5,7) is convolved with the image.
    2. A pixel element in the original image is ‘1’ if at least one pixel under the kernel is ‘1’.
    3. It increases the white region in the image or the size of the foreground object increases.
"""

import cv2
import numpy as np

img = cv2.imread('img1.jpg', 0)

kernel = np.ones((5, 5), np.uint8)

img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
