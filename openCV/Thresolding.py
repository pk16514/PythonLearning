"""
--> Simple Thresholding

Thresholding is a technique in OpenCV, which is the assignment of pixel values in relation to the
threshold value provided. In thresholding, each pixel value is compared with the threshold value.
If the pixel value is smaller than the threshold, it is set to 0, otherwise, it is set to a maximum
value (generally 255). Thresholding is a very popular segmentation technique, used for separating an
object considered as a foreground from its background. A threshold is a value which has two regions on
its either side i.e. below the threshold or above the threshold.

In Computer Vision, this technique of thresholding is done on grayscale images. So initially, the image
has to be converted in grayscale color space.

The basic Thresholding technique is Binary Thresholding. For every pixel, the same threshold value is
applied.
The different Simple Thresholding Techniques are:
check 'SimpleThresoldingTypes.png'
    cv2.THRESH_BINARY: dst(x,y) = maxval if src(x, y) > thresold else 0
    cv2.THRESH_BINARY_INV: dst(x,y) = 0 if src(x, y) > thresold else maxval
    cv.THRESH_TRUNC: dst(x,y) = thresold if src(x, y) > thresold else src(x, y)
    cv.THRESH_TOZERO: dst(x,y) = src(x, y) if src(x, y) > thresold else 0
    cv.THRESH_TOZERO_INV: dst(x,y) = 0 if src(x, y) > thresold else src(x, y)

Syntax: cv2.threshold(source, thresholdValue, maxVal, thresholdingTechnique)
Parameters:
        source: Input Image array (must be in Grayscale).
        thresholdValue: Value of Threshold below and above which pixel values will change accordingly.
        maxVal: Maximum value that can be assigned to a pixel.
        thresholdingTechnique: The type of thresholding to be applied.

--> Adaptive Thresolding

Another Thresholding technique is Adaptive Thresholding. In Simple Thresholding, a global value of
threshold was used which remained constant throughout. So, a constant threshold value won’t help in
the case of variable lighting conditions in different areas. Adaptive thresholding is the method where
the threshold value is calculated for smaller regions. This leads to different threshold values for
different regions with respect to the change in lighting. We use cv2.adaptiveThreshold for this.

Syntax: cv2.adaptiveThreshold(source, maxVal, adaptiveMethod, thresholdType, blocksize, constant)
Parameters:
        source: Input Image array(Single-channel, 8-bit or floating-point)
        maxVal: Maximum value that can be assigned to a pixel.
        adaptiveMethod: Adaptive method decides how threshold value is calculated.
            1. cv2.ADAPTIVE_THRESH_MEAN_C:
               Threshold Value = (Mean of the neighbourhood area values – constant value).
               In other words, it is the mean of the blockSize×blockSize neighborhood of a point minus
               constant.

            2. cv2.ADAPTIVE_THRESH_GAUSSIAN_C:
               Threshold Value = (Gaussian-weighted sum of the neighbourhood values – constant value).
               In other words, it is a weighted sum of the blockSize×blockSize neighborhood of a point
               minus constant.

        thresholdType: The type of thresholding to be applied. It can only be either cv2.THRESH_BINARY or
                       cv2.THRESH_BINARY_INV
        blockSize: Size of a pixel neighborhood that is used to calculate a threshold value.
        constant: A constant value that is subtracted from the mean or weighted sum of the neighbourhood
                  pixels.

--> Otsu Thresolding

In Otsu Thresholding, a value of the threshold isn’t chosen but is determined automatically. A bimodal
image (two distinct image values) is considered. The histogram generated contains two peaks. So, a
generic condition would be to choose a threshold value that lies in the middle of both the histogram
peak values.

We use the Traditional cv2.threshold function and use cv2.THRESH_OTSU as an extra flag.
Syntax is similar to Simple Thresolding.
"""

import cv2
import numpy as np

img = cv2.imread('cat.png', 0)

# Simple Thresolding

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)

# Adaptive Thresolding

thresh6 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5)

thresh7 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)

cv2.imshow('Adaptive Mean', thresh6)
cv2.imshow('Adaptive Gaussian', thresh7)

# Otsu Thresolding

ret, thresh8 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(ret)
cv2.imshow('Otsu Threshold', thresh8)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
