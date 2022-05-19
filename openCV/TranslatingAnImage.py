import cv2
import numpy as np

# Create translation matrix.
# If the shift is (x, y) then matrix would be
# M = [[1 0 x]
#      [0 1 y]]
# Let's shift by (100, 50).
M = np.float32([[1, 0, 100], [0, 1, 50]])

img = cv2.imread('goldygopher.png')
(col, row) = img.shape[:2]

res = cv2.warpAffine(img, M, (row, col))

cv2.imshow('Image', res)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
