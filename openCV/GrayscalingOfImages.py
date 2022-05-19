"""
Grayscaling is the process of converting an image from other color spaces e.g. RGB, CMYK, HSV, etc. to
shades of gray. It varies between complete black and complete white.

Importance of grayscaling
    Dimension reduction: For example, In RGB images there are three color channels and has three
                         dimensions while grayscale images are single-dimensional.
    Reduces model complexity: Consider training neural article on RGB images of 10x10x3 pixel. The input
                              layer will have 300 input nodes. On the other hand, the same neural network
                              will need only 100 input nodes for grayscale images.
    For other algorithms to work: Many algorithms are customized to work only on grayscale images
                                  e.g. Canny edge detection function pre-implemented in OpenCV library
                                  works on Grayscale images only.
"""

# Method 1: Using the cv2.cvtColor() function

import cv2

image = cv2.imread('cat.png')
cv2.imshow('Original', image)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image1', gray_image)

# Method 2: Using the cv2.imread() function with flag = zero

img = cv2.imread('cat.png', 0)
cv2.imshow('Grayscale Image2', img)

# Method 3: Using the pixel manipulation (Average method)

img = cv2.imread('cat.png')

(col, row) = img.shape[0:2]

for i in range(col):
    for j in range(row):
        img[i, j] = sum(img[i, j]) * 0.33

cv2.imshow('Grayscale Image3', img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
