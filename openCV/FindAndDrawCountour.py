"""
1. Contours are defined as the line joining all the points along the boundary of an image that are
   having the same intensity. Contours come handy in shape analysis, finding the size of the object
   of interest, and object detection.

2. contours(mentioned in code) is a python list of all the contours in the image. Each individual contour
   is a Numpy array of (x, y) coordinates of boundary points of the object.
"""

import numpy as np
import cv2

img = cv2.imread('goldygopher.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))
print(contours[0].shape)

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.drawContours(imgray, contours, -1, (0, 255, 0), 3)

cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()
