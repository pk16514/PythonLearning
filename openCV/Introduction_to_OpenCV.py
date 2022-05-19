"""
# Rotating an Image

There are a lot of steps involved in rotating an image. So, let me explain each of them in detail.
The 2 main functions used here are –
    getRotationMatrix2D()
    warpAffine()

--> getRotationMatrix2D()
    It takes 3 arguments –
        center – The center coordinates of the image
        Angle – The angle (in degrees) by which the image should be rotated
        Scale – The scaling factor

        It returns a 2*3 matrix consisting of values derived from alpha and beta
        α = scale * cos(angle)
        β = scale * sin(angle)

        [(α, −β) (β, α) ((1−α)⋅center.x−β⋅center.y, β⋅center.x+(1−α)⋅center.y)]

--> warpAffine()
    The function warpAffine transforms the source image using the rotation matrix:
        dst(x, y) = src(M11X + M12Y + M13, M21X + M22Y + M23)
    Here M is the rotation matrix, described above.
    It calculates new x, y co-ordinates of the image and transforms it.

# Drawing a Rectangle

It takes in 5 arguments –
    Image
    Top-left corner co-ordinates
    Bottom-right corner co-ordinates
    Color (in BGR format)
    Line width

# Displaying Text

It takes in 7 arguments –
    Image
    Text to be displayed
    Bottom-left corner co-ordinates, from where the text should start
    Font
    Font size
    Color (BGR format)
    Line width
"""

import cv2

# -------------Reading_an_Image--------------------

image = cv2.imread('road.jpg')
# cv2.IMREAD_COLOR OR 1 is default value
# image = cv2.imread('road.jpg', cv2.IMREAD_COLOR)
# image = cv2.imread('road.jpg', 1)
# image = cv2.imread('road.jpg', cv2.IMREAD_GRAYSCALE)
# image = cv2.imread('road.jpg', 0)
# image = cv2.imread('road.jpg', cv2.IMREAD_UNCHANGED)
# image = cv2.imread('road.jpg', -1)

cv2.imshow('output1', image)

h, w, ch = image.shape

print("Height = {},  Width = {}".format(h, w))

# -----Extracting the RGB values of a pixel---------

(B, G, R) = image[100, 100]

print("R = {}, G = {}, B = {}".format(R, G, B))


R = image[100, 100, 2]
print("R = {}".format(R))

G = image[100, 100, 1]
print("G = {}".format(G))

B = image[100, 100, 0]
print("B = {}".format(B))

# -----Extracting the Region of Interest (ROI)-------

roi = image[100:500, 200:700]

cv2.imshow('output2', roi)

# -------------Resizing the Image--------------------

resize = cv2.resize(image, (800, 800))

ratio = 800 / w
dim = (800, int(h * ratio))

resize_aspect = cv2.resize(image, dim)

cv2.imwrite('road_resize.png', resize_aspect)

cv2.imshow('output3', resize_aspect)

# -------------Rotating the Image--------------------

center_pixel = (w // 2, h // 2)

matrix = cv2.getRotationMatrix2D(center_pixel, -45, 1.0)

rotated = cv2.warpAffine(image, matrix, (w, h))

cv2.imshow('output4', rotated)

# -------------Drawing a Rectangle--------------------

output = image.copy()

rectangle = cv2.rectangle(output, (1500, 900), (600, 400), (255, 0, 0), 2)

cv2.imshow('output5', rectangle)

# -------------Drawing a Rectangle--------------------

output = image.copy()

text = cv2.putText(output, 'OpenCV Demo', (100, 150), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)

cv2.imshow('output6', text)

# ---Visualizing the different color channels of an RGB image---

B, G, R = cv2.split(image)

cv2.imshow("output7", image)
cv2.imshow("output8", B)
cv2.imshow("output9", G)
cv2.imshow("output10", R)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
