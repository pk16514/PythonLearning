"""
Filters

The current version of pillow library provides below mentioned set of predefined image enhancement filters.
    BLUR
    CONTOUR
    DETAIL
    EDGE_ENHANCE
    EDGE_ENHANCE_MORE
    EMBOSS
    FIND_EDGES
    SHARPEN
    SMOOTH
    SMOOTH_MORE
"""

from PIL import Image, ImageFilter

from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN)


img = Image.open('cat.png')

# img1 = img.filter(BLUR)
# img1 = img.filter(CONTOUR)
# img1 = img.filter(DETAIL)
img1 = img.filter(EDGE_ENHANCE)
# img1 = img.filter(EDGE_ENHANCE_MORE)
# img1 = img.filter(EMBOSS)
# img1 = img.filter(FIND_EDGES)
# img1 = img.filter(SMOOTH)
# img1 = img.filter(SMOOTH_MORE)
# img1 = img.filter(SHARPEN)
img1.save('cat_filter.png')
img1.show()
