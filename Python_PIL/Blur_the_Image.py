"""
Blurring an image can be done by reducing the level of noise in the image by applying a filter to
an image. Image blurring is one of the important aspects of image processing.

The ImageFilter class in the Pillow library provides several standard image filters. Image filters can
be applied to an image by calling the filter() method of Image object with required filter type as
defined in the ImageFilter class.

There are various techniques used to blur images and we are going to discuss the below mentioned techniques.
--> Simple blur
--> Box blur
--> Gaussian blur

All these three techniques are going to use ‘Image.filter()’ method for applying the filter to images.

- Simple blur

It applies a blurring effect on to the image as specified through a specific kernel or a convolution matrix.
Syntax: filter(ImageFilter.BLUR)

- Box blur

In this filter, we use ‘radius’ as parameter. Radius is directly proportional to the blur value.
The blurred color of the current pixel is the average of the current pixel’s color and its 2*Radius(i.e 4 = 8) neighboring
pixels. Box blur is also known as box linear filter.
Syntax: ImageFilter.BoxBlur(radius)
Where-
    Radius − Size of the box in one direction.
    Radius 0 − means no blurring & returns the same image.

- Gaussian Blur

This filter also uses parameter radius and does the same work as box blur with some algorithmic changes.
In short, changing the radius value, will generate different intensity of ‘Gaussianblur’ images.
Syntax: ImageFilter.GaussianBlur(radius=2)
Where-
    Radius – Blur radius
"""

from PIL import Image, ImageFilter

# Simple Blur

image1 = Image.open('img1.jpg')
blurImage1 = image1.filter(ImageFilter.BLUR)
blurImage1.show()

# Box Blur

image2 = Image.open('img1.jpg')
blurImage2 = image2.filter(ImageFilter.BoxBlur(5))
blurImage2.show()

# Gaussian Blur

image3 = Image.open('img1.jpg')
blurImage3 = image3.filter(ImageFilter.GaussianBlur(4))
blurImage3.show()
