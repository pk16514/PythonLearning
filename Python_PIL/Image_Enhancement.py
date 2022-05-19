"""
The ImageEnhance module contains various classes which will be used for image enhancement.
Classes We Can Use For Enhancement-
All enhancement classes implement a typical interface, containing one method which is named the
‘enhance(factor)’ method

Syntax: PIL.ImageEnhance.[method](image_variable_name)
        The method can be brightness, color, contrast, sharpness.

        Parameter: The enhance() method takes just one parameter factor, i.e. a floating-point.
        Return Type: This method returns an enhanced image.
"""

from PIL import Image
from PIL import ImageEnhance

image = Image.open('cat.png')

# --------------Brightness()-----------------

"""
Adjust image brightness. It’s accustomed to controlling the brightness of our resulting image.
An enhancement factor of 0.0 results in a full black image and an enhancement factor of 1.0 results
the same as the original image.
The code for brightness goes like below:
"""

curr_bri = ImageEnhance.Brightness(image)
new_bri = 2.5

img_brightened = curr_bri.enhance(new_bri)
# img_brightened.show()

# -----------------Color()---------------------

"""
Adjust image color level. It’s accustomed to controlling the color level of our resulting image.
An enhancement factor of 0.0 results in a full black and white image and an enhancement factor of 1.0
results the same as the original image.An enhancement factor of 0.0 results in a full black and white image and an enhancement factor of 1.0 results the same as the original image.
The code for coloring goes like below:
"""

curr_col = ImageEnhance.Color(image)
new_col = 2.5

img_colored = curr_col.enhance(new_col)
# img_colored.show()

# -----------------Contrast()-------------------

"""
Adjust image Contrast. It is accustomed to controlling the contrast of our resulting image.
An enhancement factor of 0.0 results in a full grey image and an enhancement factor of 1.0
results the same as the original image.
The code for changing contrast goes like below:
"""

curr_con = ImageEnhance.Contrast(image)
new_con = 0.3

img_contrasted = curr_con.enhance(new_con)
# img_contrasted.show()

# ------------------Sharpness()------------------

"""
Adjust image Sharpness. It’s accustomed to controlling the sharpness of our resulting image.
An enhancement factor of 0.0 results in a blurred image and an enhancement factor of 1.0 results
in the same as the original image and a factor > 1.0 results in a sharpened image.
The code for changing sharpness goes like below:
"""

curr_sharp = ImageEnhance.Sharpness(image)
new_sharp = 8.3

img_sharped = curr_sharp.enhance(new_sharp)
img_sharped.show()
