import numpy as np
import cv2
from matplotlib import pyplot as plt 

# 1. Feature Detection Algorithm

# 1.1 Harris Corner Detection

# input_img = 'Taj-Mahal-Agra-India.jpg'
# ori = cv2.imread(input_img)
# image = cv2.imread(input_img)
# gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray,2,3,0.04)
# dst = cv2.dilate(dst,None)
# image[dst>0.01*dst.max()]=[0,0,255]
# cv2.imshow('Original',ori) 
# cv2.imshow('Harris',image)
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()

# 1.2 Shi-Tomasi Corner Detector

# img = cv2.imread('Taj-Mahal-Agra-India.jpg')
# ori = cv2.imread('Taj-Mahal-Agra-India.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# corners = cv2.goodFeaturesToTrack(gray,20,0.01,10)
# corners = np.int0(corners) 
# for i in corners:
#     x,y = i.ravel()
#     cv2.circle(img,(x,y),3,255,-1) 
# cv2.imshow('Original', ori)
# cv2.imshow('Shi-Tomasi', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 2. Detection of blobs

# import cv2
# import numpy as np;
# ori = cv2.imread('Taj-Mahal-Agra-India.jpg')
# im = cv2.imread('Taj-Mahal-Agra-India.jpg', cv2.IMREAD_GRAYSCALE)
# detector = cv2.SimpleBlobDetector_create()
# keypoints = detector.detect(im)
# im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv2.imshow('Original',ori) 
# cv2.imshow('BLOB',im_with_keypoints)
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()

# 3. Feature Descriptor Algorithms

