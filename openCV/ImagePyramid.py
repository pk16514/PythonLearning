"""
Image Pyramids are one of the most beautiful concept of image processing.Normally, we work with images
with default resolution but many times we need to change the resolution (lower it) or resize the original
image in that case image pyramids comes handy.

Types of Pyramid:
    1. Gaussian Pyramid
    2. Laplacian Pyramid

--> Gaussian Pyramid-

The pyrUp() function increases the size to double of its original size and pyrDown() function decreases
the size to half. If we keep the original image as a base image and go on applying pyrDown function
on it and keep the images in a vertical stack, it will look like a pyramid. The same is true for
upscaling the original image by pyrUp function.

Once we scale down and if we rescale it to the original size, we lose some information and the resolution
of the new image is much lower than the original one.

Pyramid Representation is a type of multi-scale signal representation in which a signal or an image
is subject to repeated smoothing and Sub-sampling.

--> Laplacian Pyramid-

Laplacian Pyramids are formed from the gaussian pyramid. There is no exclusive function for creating the
laplacian pyramid.

A level in Laplacian Pyramid is formed by the difference between that level in Gaussian Pyramid and
extended version of its upper level in Gaussian Pyramid.

Advantages of Image pyramids:
    Lowering of resolution
    Getting various sizes of image
    Image Blending
    Edge detection

Note:- Image shape(height, width) should be even. If not then resize.
"""

# Lowering the resolution
from PIL import Image
import cv2
import numpy as np
from numpy import asarray
import matplotlib.pyplot as plt

img1 = cv2.imread("cat.png")

layer1 = img1.copy()

for i in range(4):
    plt.subplot(2, 2, i + 1)

    layer1 = cv2.pyrDown(layer1)

    plt.imshow(layer1)
    cv2.imshow('img1' + str(i), layer1)

plt.show()

# Image Blending


def gaussian_pyramid(img, num_levels):
    lower = img.copy()
    gaussian_pyr = [lower]
    for i in range(num_levels):
        lower = cv2.pyrDown(lower)
        gaussian_pyr.append(np.float32(lower))
    return gaussian_pyr


def laplacian_pyramid(gaussian_pyr):
    laplacian_top = gaussian_pyr[-1]
    num_levels = len(gaussian_pyr) - 1
    laplacian_pyr = [laplacian_top]
    for i in range(num_levels, 0, -1):
        size = (gaussian_pyr[i - 1].shape[1], gaussian_pyr[i - 1].shape[0])
        gaussian_expanded = cv2.pyrUp(gaussian_pyr[i], dstsize=size)
        laplacian = cv2.subtract(gaussian_pyr[i - 1], gaussian_expanded, dtype=cv2.CV_32F)
        laplacian_pyr.append(laplacian)
    return laplacian_pyr


def blend(laplacian_A, laplacian_B, mask_pyr):
    LS = []
    for la, lb, mask in zip(laplacian_A, laplacian_B, mask_pyr):
        ls = lb * mask + la * (1.0 - mask)
        LS.append(ls)
    return LS


def reconstruct(laplacian_pyr):
    laplacian_top = laplacian_pyr[0]
    laplacian_lst = [laplacian_top]
    num_levels = len(laplacian_pyr) - 1
    for i in range(num_levels):
        size = (laplacian_pyr[i + 1].shape[1], laplacian_pyr[i + 1].shape[0])
        laplacian_expanded = cv2.pyrUp(laplacian_top, dstsize=size)
        laplacian_top = cv2.add(laplacian_pyr[i + 1], laplacian_expanded)
        laplacian_lst.append(laplacian_top)
    return laplacian_lst


if __name__ == '__main__':
    img1 = cv2.imread('cloud.jpg')
    img1 = cv2.resize(img1, (1800, 1000))
    img2 = cv2.imread('jet.jpg')
    img2 = cv2.resize(img2, (1800, 1000))

    mask = np.zeros((1000, 1800, 3), dtype='float32')
    mask[250:500, 640:1440, :] = (1, 1, 1)
    # mask = np.zeros((512, 512, 3), dtype='float32')
    # mask[:, 256:, :] = (1, 1, 1)

    num_levels = 7

    gaussian_pyr_1 = gaussian_pyramid(img1, num_levels)
    laplacian_pyr_1 = laplacian_pyramid(gaussian_pyr_1)

    gaussian_pyr_2 = gaussian_pyramid(img2, num_levels)
    laplacian_pyr_2 = laplacian_pyramid(gaussian_pyr_2)

    mask_pyr_final = gaussian_pyramid(mask, num_levels)
    mask_pyr_final.reverse()

    add_laplace = blend(laplacian_pyr_1, laplacian_pyr_2, mask_pyr_final)

    final = reconstruct(add_laplace)

cv2.imwrite('pp2.jpg', final[num_levels])
pic = cv2.imread('pp2.jpg')
cv2.imshow('xyz', pic)

picture = Image.open('pp2.jpg')
cv2.imshow('wxyz', asarray(picture))
picture.show()

# Edge Detection(Using Concept of Laplacian Pyramid)

img2 = cv2.imread("window.jpg")
layer2 = img2.copy()
gaussian_pyramid_list = [layer2]

for i in range(6):
    layer2 = cv2.pyrDown(layer2)
    gaussian_pyramid_list.append(layer2)
    cv2.imshow('img2' + str(i), layer2)

layer2 = gaussian_pyramid_list[6]
cv2.imshow('upper level Gaussian Pyramid', layer2)
laplacian_pyramid_list = [layer2]

for i in range(6, 0, -1):
    size = (gaussian_pyramid_list[i - 1].shape[1], gaussian_pyramid_list[i - 1].shape[0])
    gaussian_extended = cv2.pyrUp(gaussian_pyramid_list[i], dstsize=size)
    laplacian = cv2.subtract(gaussian_pyramid_list[i - 1], gaussian_extended)
    cv2.imshow('img3' + str(i), laplacian)

cv2.imshow("Original image", img2)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
