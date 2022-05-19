from PIL import Image, ImageDraw, ImageEnhance, ImageFont
from IPython.display import display

file = "MichiganCoverPhoto.png"
image = Image.open(file).convert('RGB')

images = []
for i in range(3):
    for j in range(3):
        small_sheet = Image.new('RGB', (image.width, image.height + 50), (0, 0, 0))
        draw = ImageDraw.Draw(small_sheet)
        font = ImageFont.truetype('Jupyter_Notebook/py3/readonly/fanwood-webfont.ttf', 50)
        text = 'channel {} intensity {}'.format(i, (4 * j + 1) / 10)
        draw.text((0, image.height), text, font=font)
        small_sheet.paste(image, (0, 0))
        images.append(small_sheet)

new_images = []
new_bri = 0.1

for image in images[:3]:
    r, g, b = image.split()
    curr_bri = ImageEnhance.Brightness(r)
    brightened_image = curr_bri.enhance(new_bri)
    photo1 = Image.merge('RGB', (brightened_image, g, b))
    new_images.append(photo1)
    new_bri += 0.4

new_bri = 0.1

for image in images[3:6]:
    r, g, b = image.split()
    curr_bri = ImageEnhance.Brightness(g)
    brightened_image = curr_bri.enhance(new_bri)
    photo1 = Image.merge('RGB', (r, brightened_image, b))
    new_images.append(photo1)
    new_bri += 0.4

new_bri = 0.1

for image in images[6:]:
    r, g, b = image.split()
    curr_bri = ImageEnhance.Brightness(b)
    brightened_image = curr_bri.enhance(new_bri)
    photo1 = Image.merge('RGB', (r, g, brightened_image))
    new_images.append(photo1)
    new_bri += 0.4


contact_sheet = Image.new('RGB', (small_sheet.width * 3, small_sheet.height * 3), color=(0, 0, 0))
x = 0
y = 0

for image in new_images:
    contact_sheet.paste(image, (x, y))

    if x + image.width == contact_sheet.width:
        x = 0
        y += image.height
    else:
        x += image.width

contact_sheet = contact_sheet.resize((int(contact_sheet.width / 2), int(contact_sheet.height / 2)))
contact_sheet.show()
display(contact_sheet)
