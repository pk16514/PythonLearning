"""
alpha_composite(im1, im2)
        Alpha composite im2 over im1.
        im1: The first image. Must have mode RGBA.
        im2: The second image. Must have mode RGBA, and the same size as
             the first image.
        returns: An :py:class:`~PIL.Image.Image` object.
"""

from PIL import Image, ImageDraw, ImageFont

img1 = Image.open('cat.png').convert('RGBA')
text = Image.new('RGBA', img1.size, (255, 255, 255, 0))

draw = ImageDraw.Draw(text)
font = ImageFont.truetype('Jupyter_Notebook/py3/readonly/fanwood-webfont.ttf', 40)

draw.text((25, 25), "Cats Lover", font=font, fill=(255, 255, 255, 128))
out = Image.alpha_composite(img1, text)
out.show()
