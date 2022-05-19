import cv2
import numpy as np

image = cv2.imread('cat.png', 0)

binary = cv2.threshold(image, 100, 255, 2)
print(binary)
cv2.imshow('Binary Image', binary[1])

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
