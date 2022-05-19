"""
1. Color               Red               Green               Blue
    Red                255                 0                   0
    Green               0                 255                  0
    Blue                0                  0                  255
    White              255                255                 255
    Black               0                  0                   0
    Yellow             255                255                  0
    Magenta            255                 0                  255

2. Each Pixel object has three attributes: the red intensity, the green
   intensity, and the blue intensity. A pixel provides three methods
   that allow us to ask for the intensity values. They are called getRed,
   getGreen, and getBlue. In addition, we can ask a pixel to change an
   intensity value using its setRed, setGreen, and setBlue methods.

3. Method Name          Example                    Explanation
   Pixel(r,g,b)     Pixel(20,100,50)     Create a new pixel with 20 red,
                                                100 green, and 50 blue.
   getRed()         r = p.getRed()      Return the red component intensity
   getGreen()       r = p.getGreen()    Return the green component intensity
   getBlue()        r = p.getBlue()     Return the blue component intensity
   setRed()         p.setRed(100)       set the red component intensity to 100
   setGreen()       p.setGreen(45)      set the green component intensity to 45
   setBlue()        p.setBlue(156)      set the blue component intensity to 156

4. To access the pixels in a real image, we need to first create an Image
   object. Image objects can be created in two ways. First, an Image object can
   be made from the files that store digital images. The image object has an
   attribute corresponding to the width, the height, and the collection of
   pixels in the image.

   Method Name              Example                     Explanation
   Image(filename)  img = image.Image(“cy.png”)      Create an Image object
                                                     from the file cy.png.
   EmptyImage()     img = image.EmptyImage(100,200)  Create an Image object
                                                    that has all “White” pixels
   getWidth()           w = img.getWidth()           Return the width of the
                                                     image in pixels.
   getHeight()          w = img.getHeight()          Return the height of the
                                                     image in pixels.
   getPixel(col,row) p = img.getPixel(35,86)         Return the pixel at column
                                                     35, row 86.
   setPixel(col,row,p) img.setPixel(35,86, mp)       Set the pixel at column
                                                     100, row 50 to be mp.
   Note- (col, row) represents the position not the no. of cols. & rows.
"""

# Program-1


import image

p = image.Pixel(45, 76, 200)
print(p.getRed())
p.setRed(66)
print(p.getRed())
p.setBlue(p.getGreen())
print(p.getGreen(), p.getBlue())
print()

# Program-2


img = image.Image("luther.jpg")

print(img.getWidth())
print(img.getHeight())

p = img.getPixel(45, 55)
print(p.getRed(), p.getGreen(), p.getBlue())

# Program-3(Negative Image)


img = image.Image('luther.jpg')
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        new_red = 255 - p.getRed()
        new_green = 255 - p.getGreen()
        new_blue = 255 - p.getBlue()

        newPixel = image.Pixel(new_red, new_green, new_blue)
        img.setPixel(col, row, newPixel)

img.draw(win)
win.exitonclick()

# Program-4(GreyScale Image)

img = image.Image('goldygopher.png')
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        new_red = (p.getRed() + p.getGreen() + p.getBlue()) // 3
        new_green = (p.getRed() + p.getGreen() + p.getBlue()) // 3
        new_blue = (p.getRed() + p.getGreen() + p.getBlue()) // 3

        newPixel = image.Pixel(new_red, new_green, new_blue)
        img.setPixel(col, row, newPixel)

img.draw(win)
win.exitonclick()
