"""
# check image Erosion&Dilation.png
In erosion, Black pixel increases White pixel decreases but In dilation, Black Pixel decreases White pixel
increses. In case of Erosion, keep the Black pixel(0) as it is and in case of dilation keep the white pixel(1)
as it is.
"""

import cv2
import numpy as np

path = 'cat.png'

image = cv2.imread(path, 0)
kernel = np.ones((5, 5), np.uint8)

image = cv2.erode(image, kernel, iterations=1)

cv2.imshow('Image', image)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
