"""
Syntax: Image.merge(mode, bands)
where-
    mode − The mode to use for the output image.
    bands − A sequence containing one single-band image for each band in the output image. All bands
            must have the same size.
    Return value − An Image objects.
"""

from PIL import Image

photo = Image.open("img1.jpg")
r, g, b = photo.split()
# image.show()
photo1 = Image.merge("RGB", (b, g, r))
photo1.show()
