"""
The process of image detection involves detecting sharp edges in the image. This edge detection
is essential in context of image recognition or object localization/detection. There are several
algorithms for detecting edges due to it’s wide applicability. We’ll be using one such algorithm
known as Canny Edge Detection.

Syntax: cv2.Canny(image, edges, threshold1, threshold2)
Parameters −
        image − A Mat object representing the source (input image) for this operation.
        edges − A Mat object representing the destination (edges) for this operation.
        threshold1 − A variable of the type double representing the first threshold for the
                     hysteresis procedure.
        threshold2 − A variable of the type double representing the second threshold for the
                     hysteresis procedure.
"""

import cv2
import numpy as np

img = cv2.imread('window.jpg')

edges = cv2.Canny(img, 100, 200)
cv2.imshow('Image', edges)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
