"""
Syntax: Image.new(mode, size, color=0)
where-
    mode: The mode to use for the new image.
    size: A 2-tuple, containing (width, height) in pixels.
    color: What color to use for the image.  Default is black. If given, this should be a single integer
           or floating point value for single-band modes, and a tuple for multi-band modes (one value
           per band).  When creating RGB images, you can also use color strings as supported by the
           ImageColor module.  If the color is None, the image is not initialised.
"""

from PIL import Image
new_img = Image.new('RGB', (800, 450), color=(4, 16, 255))
new_img.show()
