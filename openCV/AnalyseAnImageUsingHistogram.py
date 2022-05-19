"""
1. plt.hist(flatten the image array, no. of divisions of pixel range(bins), range of pixel value,
         color of bins, reative_width, histtype='step')
2. In openCV, 0 is considered 'black' and '1' is considered white only when data type is float(np.float)
3. It means that all the pixels having a value, will be added with their pixel value to the histogram
   you create. All the others will get ignored. Exactly like stated. For example if you have a squared
   image of 45x45 pixels, and a mask of 45x45 pixels with a white circle of 20 pixels diameter starting
   from the center point, then only the pixels inside the circle will be used for calculating your
   histogram.
4. Syntax: histogram = cv2.calcHist([gray_img],[0],None,[256],[0,256])
   Parameters:
            images: source image of type uint8 or float32. it should be given in as a list, ie, [gray_img].
            channels: it is also given in as a list []. It the index of channel for which we calculate
                      histogram. For example, if input is grayscale image, its value is [0]. For color
                      image, you can pass [0],[1] or [2] to calculate histogram of blue,green or red
                      channel, respectively.
            mask: mask image. To find histogram of full image, it is set as None. However, if we want
                  to get histogram of specific region of image, we should create a mask image for that
                  and give it as mask.
            histSize: this represents our BIN count. Need to be given in []. For full scale, we pass [256].
            ranges: Normally, it is [0,256].
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

gray_img = cv2.imread('cat.png')
cv2.imshow('GoldenCat', gray_img)

channel = cv2.split(gray_img)
color = ['b', 'g', 'r']

plt.xlabel('Pixel Value')
plt.ylabel('Corresponding Number of Pixels')
plt.title('Histogram for gray scale picture')

# Method-1

# histogram = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
# plt.plot(histogram)

for ch, col in enumerate(color):
    histogram = cv2.calcHist([gray_img], [ch], None, [256], [0, 256])
    plt.plot(histogram, col)

# Method-2

# plt.hist(gray_img.ravel(), 256, [0, 256], color='orange', rwidth=0.8)

for ch, col in zip(channel, color):
    plt.hist(ch.ravel(), 256, [0, 256], color=col)

plt.legend(['Blue', 'Green', 'Red'])
plt.show()

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
