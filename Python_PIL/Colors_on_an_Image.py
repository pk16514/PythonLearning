"""
---> ImageColor.getrgb() Method

Convert a color string to an RGB tuple. If the string cannot be parsed, a ValueError exception is raised
by this function.
Syntax: PIL.ImageColor.getrgb(color)
Where-
    Arguments: color – A color string
    Return Value: (red, green, blue[, alpha])

--> ImageColor.getcolor() Method

This method is same as getrgb(), however, converts the RGB value to a greyscale value, if the mode
isn’t color or a palette image. The graphics commands support shape drawing and text annotation color
or a palette image. If the string cannot be parsed, this function raises a ValueError exception.
Syntax: PIL.ImageColor.getcolor(color, mode)
Where-
    Arguments - A color string
    Return Value - (graylevel[, alpha]) or (red, green, blue[, alpha])
"""

from PIL import ImageColor

img1 = ImageColor.getrgb("blue")
print(img1)

img2 = ImageColor.getrgb("purple")
print(img2)

img3 = ImageColor.getcolor('pink', 'L')
print(img3)
