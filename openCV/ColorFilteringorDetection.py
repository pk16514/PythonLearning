"""
In OpenCV, Hue has values from 0 to 180, Saturation and Value from 0 to 255. Thus, OpenCV uses HSV
ranges between (0-180, 0-255, 0-255). In OpenCV, the H values 179, 178, 177 and so on are as close
to the true RED as H value 1, 2, 3 and so on.
"""

import cv2
import numpy as np

image = cv2.imread('rose.jpg')
cv2.imshow("Original", image)

result = image.copy()

# Method-1

image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower1 = np.array([0, 100, 20])
upper1 = np.array([10, 255, 255])

lower2 = np.array([160, 100, 20])
upper2 = np.array([179, 255, 255])

lower_mask = cv2.inRange(image, lower1, upper1)
upper_mask = cv2.inRange(image, lower2, upper2)

full_mask = lower_mask + upper_mask
result = cv2.bitwise_and(result, result, mask=full_mask)

cv2.imshow('mask', full_mask)
cv2.imshow('result', result)

# Method-2

result[(result[:, :, 0] > 110) | (result[:, :, 1] > 35) | (result[:, :, 2] < 0)] = 0

cv2.imshow('xyz', result)

# Problem(Human Image Extraction)


img = cv2.imread('jumping-people.jpg')
cv2.imshow("Original", img)

duplicate = img.copy()

duplicate[(duplicate[:, :, 0] > 25) | (duplicate[:, :, 1] > 25) | (duplicate[:, :, 2] > 25)] = 255

cv2.imshow('Human', duplicate)
cv2.waitKey(0)
cv2.destroyAllWindows()
