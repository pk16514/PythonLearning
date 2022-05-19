"""
cv2.copyMakeBorder() method is used to create a border around the image like a photo frame.

Syntax: cv2.copyMakeBorder(src, top, bottom, left, right, borderType, value)
Parameters:
        src: It is the source image.
        top: It is the border width in number of pixels in top direction.
        bottom: It is the border width in number of pixels in bottom direction.
        left: It is the border width in number of pixels in left direction.
        right: It is the border width in number of pixels in right direction.
        borderType: It depicts what kind of border to be added. It is defined by flags
                    like cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT, etc
        value: It is an optional parameter which depicts color of border if border type
               is cv2.BORDER_CONSTANT.
        Return Value: It returns an image.

The borderType flags are described below:

cv2.BORDER_CONSTANT: It adds a constant colored border. The value should be given as next argument.
cv2.BORDER_REFLECT: The border will be mirror reflection of the border elements. Suppose, if image
                    contains letters “abcdefg” then output will be “gfedcba|abcdefg|gfedcba“.
cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT: It does the same works as cv2.BORDER_REFLECT but with
                                              slight change. Suppose, if image contains letters “abcdefgh”
                                              then output will be “gfedcb|abcdefgh|gfedcba“.
cv2.BORDER_REPLICATE: It replicates the last element. Suppose, if image contains letters “abcdefgh”
                      then output will be “aaaaa|abcdefgh|hhhhh“.
"""

import cv2

image = cv2.imread('geeks4geeks.png')

image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
# image = cv2.copyMakeBorder(image, 300, 300, 300, 300, cv2.BORDER_REPLICATE)

cv2.imshow('Image', image)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
