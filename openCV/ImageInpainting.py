"""
Image inpainting is the process of removing damage, such as noises, strokes or text, on images.
It is particularly useful in the restoration of old photographs which might have scratched edges
or ink spots on them. These can be digitally removed through this method.

Image inpainting works by replacing the damaged pixels with pixels similar to the neighboring ones,
therefore, making them inconspicuous and helping them blend well with the background.
Syntax:
cv2.inpaint(src, inpaintMask, inpaintRadius, flags, dst=None)

Inpainting Algorithms –

OpenCV implements two inpainting algorithms:
1. Fast Marching Method(FMM):
   Looking at the region to be inpainted, the algorithm first starts with the boundary pixels
   and then goes to the pixels inside the boundary. It replaces each pixel to be inpainted with
   a weighted sum of the pixels in the background, with more weight given to nearer pixels and
   boundary pixels.

2. Navier-Stokes(NS):
   This algorithm is inspired by partial differential equations. Starting from the edges (known regions)
   towards the unknown regions, it propagates isophote lines (lines that join same-intensity points).
   Finally, variance in an area is minimized to fill colors.
"""

import numpy as np
import cv2

img = cv2.imread('cat_damaged.png')
mask = cv2.imread('cat_mask.png', 0)

dst1 = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)
dst2 = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

cv2.imshow('cat_inpainted1.png', dst1)
cv2.imshow('cat_inpainted2.png', dst2)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
