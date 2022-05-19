"""
Image Blurring refers to making the image less clear or distinct. It is done with the help of various
low pass filter kernels.

Advantages of blurring:
    1. It helps in Noise removal. As noise is considered as high pass signal so by the application of low
       pass filter kernel we restrict noise.
    2. It helps in smoothing the image.
    3. Low intensity edges are removed.
    4. It helps in hiding the details when necessary. For e.g. in many cases police deliberately want
       to hide the face of the victim, in such cases blurring is required.

Important types of blurring:

1. Gaussian Blurring: Gaussian blur is the result of blurring an image by a Gaussian function. It is a
                      widely used effect in graphics software, typically to reduce image noise and reduce
                      detail. It is also used as a preprocessing stage before applying our machine learning
                      or deep learning models.

2. Median Blur: The Median Filter is a non-linear digital filtering technique, often used to remove noise
                from an image or signal. Median filtering is very widely used in digital image processing
                because, under certain conditions, it preserves edges while removing noise. It is one of
                the best algorithms to remove Salt and pepper noise.

Average Blur-

Syntax: cv2.blur(src, ksize, dst=None, anchor=None, borderType=None)
Parameters-
        src- input image
        dst- output image of the same size and type as src
        ksize- blurring kernel size. Should be a tuple showing ksize.width and ksize.height
        anchor- anchor point. default value Point(-1,-1) means that the anchor is at the kernel center.
        borderType- border mode used to extrapolate pixels outside of the image.
        [cv.BORDER_CONSTANT, cv.BORDER_REPLICATE, cv.BORDER_REFLECT, cv.BORDER_WRAP, cv.BORDER_REFLECT_101,
         cv.BORDER_TRANSPARENT, cv.BORDER_REFLECT101, cv.BORDER_DEFAULT, cv.BORDER_ISOLATED]


Gaussian Blur-

Syntax: cv2.GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)
Parameters-
        src- It is used to input an Image.
        dst- output image of the same size and type as src
        ksize- blurring kernel size. Should be a tuple and both should be odd and greater > 1.
        sigmaX - Kernel standard derivation along X-axis.(horizontal direction).
        sigmaY - Kernel standard derivation along Y-axis (vertical direction).
                 If sigmaY = 0 then sigmaX value is taken for sigmaY.
                 if both sigmas are zeros, they are computed from ksize.width and ksize.height respectively
        borderType- border mode used to extrapolate pixels outside of the image.
        [cv.BORDER_CONSTANT, cv.BORDER_REPLICATE, cv.BORDER_REFLECT, cv.BORDER_WRAP, cv.BORDER_REFLECT_101,
         cv.BORDER_TRANSPARENT, cv.BORDER_REFLECT101, cv.BORDER_DEFAULT, cv.BORDER_ISOLATED]

MedianBlur-

Syntax: cv2.medianBlur(src, ksize, dst=None)
Parameters-
        src- 1, 3 or 4-channel input image
        dst- destination array of the same size and type as src
        ksize- aperture linear size. it must be odd and greater than 1
"""

# check kernel.jpg

import cv2
import numpy as np

image = cv2.imread('fruits.jpg')

cv2.imshow('Original Image', image)

Average = cv2.blur(image, (6, 4), cv2.BORDER_REFLECT)
# Average = cv2.blur(image, (6, 4))
cv2.imshow('Average Blurring', Average)

Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)

median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
