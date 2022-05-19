# ---------------Opening and displaying an image----------------

from PIL import Image
file = 'cy.png'
image = Image.open(file)
# image.show()

# -----------------Attributes of Image Module--------------------

# rotate
rotated_img = image.rotate(45)
rotated_img.show()

# filename
print(image.filename)

# format
print(image.format)

# size
print(image.size)

# mode
print(image.mode)

# width
print(image.width)

# height
print(image.height)

# info
print(image.info)

# palette
print(image.palette)

# flip
vertically_flipped_img = image.transpose(method=Image.FLIP_TOP_BOTTOM)
# vertically_flipped_img.show()
horizontally_flipped_img = image.transpose(method=Image.FLIP_LEFT_RIGHT)
# horizontally_flipped_img.show()
rotated_90_img = image.transpose(method=Image.ROTATE_90)
# rotated_90_img.show()
