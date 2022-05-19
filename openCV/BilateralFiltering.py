"""
3. Bilateral Blur: A bilateral filter is a non-linear, edge-preserving, and noise-reducing smoothing filter
                   for images. It replaces the intensity of each pixel with a weighted average of intensity
                   values from nearby pixels. This weight can be based on a Gaussian distribution. Thus,
                   sharp edges are preserved while discarding the weak.
   Syntax- cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType=None)
   Parameters-
       d: Diameter of each pixel neighborhood.
       sigmaColor: Value of sigma in the color space. The greater the value, the colors farther to each
                   other will start to get mixed.
       sigmaSpace: Value of sigma in the coordinate space. The greater its value, the more further
                   pixels will mix together, given that their colors lie within the sigmaColor range.
"""
import cv2
import numpy as np

image = cv2.imread('taj.jpg')

bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
