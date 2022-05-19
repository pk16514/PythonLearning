"""
Intensity transformations are applied on images for contrast manipulation or image thresholding.
These are in the spatial domain, i.e. they are performed directly on the pixels of the image at hand, as opposed to being performed on the Fourier transform of the image.
The following are commonly used intensity transformations:
    Image Negatives (Linear)
    Log Transformations
    Power-Law (Gamma) Transformations
    Piecewise-Linear Transformation Functions
"""

import cv2
import numpy as np

img = cv2.imread('sample.jpg')

# Image Negatives(Linear)

Img_Neg = np.array(img, dtype=np.uint8)

cv2.imshow('Img1', 255 - Img_Neg)

# Log Transformations

c = 255 / (np.log(1 + np.max(img)))
log_transformed = c * np.log(1 + img)

log_transformed = np.array(log_transformed, dtype=np.uint8)

cv2.imshow('log_transformed.jpg', log_transformed)

# Power-Law (Gamma) Transformation

for gamma in [0.1, 0.5, 1.2, 2.2]:
    gamma_corrected = np.array(255 * (img / 255) ** gamma, dtype='uint8')
    cv2.imshow('gamma_transformed' + str(gamma), gamma_corrected)

# Piecewise-Linear Transformation Functions


def pixelVal(pix, r1, s1, r2, s2):
    if (0 <= pix and pix <= r1):
        return (s1 / r1) * pix
    elif (r1 < pix and pix <= r2):
        return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2) / (255 - r2)) * (pix - r2) + s2


r1 = 70
s1 = 0
r2 = 140
s2 = 255

# Vectorize the function to apply it to each value in the Numpy array.
pixelVal_vec = np.vectorize(pixelVal)

# Apply contrast stretching.
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)

cv2.imshow('contrast_stretch', contrast_stretched)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
