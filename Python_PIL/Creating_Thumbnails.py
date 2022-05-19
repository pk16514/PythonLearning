"""
Syntax: Image.thumbnail(size, resample=3)
where-
    Size − Required size
    Resample − Optional resampling filter. It can be one of these PIL.Image.NEAREST, PIL.Image.BILINEAR,
            PIL.Image.BICUBIC, or PIL.Image.LANCZOS. If omitted, it defaults to PIL.Image.BICUBIC.
    Returns − None
"""

from PIL import Image

pic = Image.open('goldygopher.png')
pic.thumbnail((90, 90), resample=3)
pic.save('goldygopher_thumbnail.jpg')
pic1 = Image.open('goldygopher_thumbnail.jpg')
pic1.show()
