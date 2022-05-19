from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


image = Image.open('luther.jpg')
width, height = image.size

draw = ImageDraw.Draw(image)

text = 'Famous Bell of Luther College'
font = ImageFont.truetype('Jupyter_Notebook/py3/readonly/fanwood-webfont.ttf', 24)

textwidth, textheight = draw.textsize(text, font)

margin = 0
x = width - textwidth - margin
y = height - textheight - margin

draw.text((x / 2, y), text, font=font, fill=(55, 128, 55), stroke_width=1)
image.show()
