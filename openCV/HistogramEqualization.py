import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Hawkes_Bay_NZ.jpg', 0)

before = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(before)
plt.title('before')

equ = cv2.equalizeHist(img)

after = cv2.calcHist([equ], [0], None, [256], [0, 256])
plt.plot(after)
plt.title('after')

plt.show()

# stacking images side-by-side
res = np.hstack((img, equ))

cv2.imshow('image', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
