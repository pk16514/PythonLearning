"""
--> Addition of Image:

We can add two images by using function cv2.add(). This directly adds up image pixels in the two images.
        Syntax: cv2.add(img1, img2)
But adding the pixels is not an ideal situation. So, we use cv2.addweighted(). Remember, both images should
be of equal size and depth.
        Syntax: cv2.addWeighted(img1, wt1, img2, wt2, gammaValue)
        Parameters:
                img1: First Input Image array(Single-channel, 8-bit or floating-point)
                wt1: Weight of the first input image elements to be applied to the final image
                img2: Second Input Image array(Single-channel, 8-bit or floating-point)
                wt2: Weight of the second input image elements to be applied to the final image
                gammaValue: Measurement of light

--> Subtraction of Image:

Just like addition, we can subtract the pixel values in two images and merge them with the help of
cv2.subtract(). The images should be of equal size and depth.
        Syntax:  cv2.subtract(src1, src2)

--> Bitwise Operations on Binary Images

Bitwise operations are used in image manipulation and used for extracting essential parts in the image.
In this article, Bitwise operations used are :
    AND- Syntax: cv2.bitwise_and(source1, source2, destination, mask)
    OR- Syntax: cv2.bitwise_or(source1, source2, destination, mask)
    XOR- Syntax: cv2.bitwise_xor(source1, source2, destination, mask)
    NOT- Syntax: cv2.bitwise_not(source, destination, mask)

    Parameters:
            source1: First Input Image array(Single-channel, 8-bit or floating-point)
            source2: Second Input Image array(Single-channel, 8-bit or floating-point)
            dest: Output array (Similar to the dimensions and type of Input image array)
            mask: Operation mask, Input / output 8-bit single-channel mask

Also, Bitwise operations helps in image masking. Image creation can be enabled with the help of these
operations. These operations can be helpful in enhancing the properties of the input images.

NOTE: The Bitwise operations should be applied on input images of same dimensions
"""

import cv2
import numpy as np

# -----------------Addition--------------------

image1 = cv2.imread('AlienAttackOnEarth.jpg')
image2 = cv2.imread('Galaxy.jpg')

weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)

cv2.imshow('Weighted Image', weightedSum)

# -----------------Subtraction--------------------

image1 = cv2.imread('star-1-300x168.jpg')
image2 = cv2.imread('dot-300x168.jpg')

Sub = cv2.subtract(image1, image2)

cv2.imshow('Subtracted Image', Sub)

# -----------------Bitwise Operations--------------------

image1 = cv2.imread('1bit1.png')
image2 = cv2.imread('2bit2.png')

# -----------------Bitwise AND--------------------

dest_and = cv2.bitwise_and(image1, image2, mask=None)

cv2.imshow('Bitwise And', dest_and)

# -----------------Bitwise OR--------------------

dest_and = cv2.bitwise_or(image1, image2, mask=None)

cv2.imshow('Bitwise Or', dest_and)

# -----------------Bitwise XOR--------------------

dest_and = cv2.bitwise_xor(image1, image2, mask=None)

cv2.imshow('Bitwise Xor', dest_and)

# -----------------Bitwise NOT--------------------

dest_not1 = cv2.bitwise_not(image1, mask=None)
dest_not2 = cv2.bitwise_not(image2, mask=None)

cv2.imshow('Bitwise NOT on image 1', dest_not1)
cv2.imshow('Bitwise NOT on image 2', dest_not2)


if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
