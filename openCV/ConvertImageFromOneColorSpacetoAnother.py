import cv2

src = cv2.imread('road_resize.png')

# image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

cv2.imshow('Image', image)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
