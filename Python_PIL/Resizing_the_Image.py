"""

Syntax: resize(size, resample=0, box=None) method of PIL.Image.
where-
    size: The requested size in pixels, as a 2-tuple: (width, height).

    resample: An optional resampling filter.  This can be one of the following from the list
                   [Image.NEAREST, Image.BOX, Image.BILINEAR, Image.HAMMING, Image.BICUBIC, Image.LANCZOS]
              If omitted, or if the image has mode "1" or "P", it is
                   set: PIL.Image.NEAREST

    box: An optional 4-tuple of floats giving the region of the source image which should be scaled.
         The values should be within (0, 0, width, height) rectangle. If omitted or None, the entire
         source is used.

    returns: Returns a resized copy of this image.

NOTE- when we print out one of the resampling values it actually just prints an integer! This is really
      common: that the API developer writes a property, such as Image.BICUBIC, and then assigns it to an
      integer value to pass it around.
"""

from PIL import Image

im = Image.open("routers.png")
resized_im = im.resize((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
# resized_im.show()

image = Image.open('Fossil.png')
new_size = (image.width * 10, image.height * 10)
# resized_image = image.resize(new_size, Image.NEAREST)
# resized_image = image.resize(new_size, Image.BOX)
# resized_image = image.resize(new_size, Image.BILINEAR)
# resized_image = image.resize(new_size, Image.HAMMING)
# resized_image = image.resize(new_size, Image.BICUBIC)
resized_image = image.resize(new_size, Image.LANCZOS)
resized_image.show()
