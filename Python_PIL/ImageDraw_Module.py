"""
Drawing Method-

1. point, line, polygon-
   line() draws a straight line connecting each point, polygon() draws a polygon where each point
   is connected , and point() draws a point of 1 pixel at each point.
   ((x1, y1), (x2, y2), (x3, y3)...)
   Point: point(xy, fill)
   Line: line(xy, fill, width)
   Polygon: polygon(xy, fill, outline)

2. Ellipse(Circle), Rectangle(Square)-
   ellipse() draws an ellipse tangent to the rectangular area specified by the argument xy. Specifying
   a square results in a true circle.
   (Upper left x coordinate, upper left y coordinate, lower right x coordinate, lower right y coordinate)
   Ellipse(Circle): ellipse(xy, fill, outline)
   Rectangle(Square): rectangle(xy, fill, outline)


3. Arc, chord, pie-
   Arc: arc(xy, start, end, fill)
        start, end
            Set the angle of the arc in degrees.
            0 degrees is the direction of 3 o'clock. clockwise.
   Chord(bow) : chord(xy, start, end, fill, outline)
                The start and end points of the arc are connected by a straight line.
   Pie : pieslice(xy, start, end, fill, outline)
         The start and end points of the arc are connected by a straight line to the center of the circle.
"""

from PIL import Image, ImageDraw

im = Image.new('RGB', (600, 300), (128, 128, 128))
draw = ImageDraw.Draw(im)

# draw.line(((30, 200), (130, 100), (80, 50)), fill=(255, 255, 0))
# draw.line(((80, 200), (180, 100), (130, 50)), fill=(255, 255, 0), width=10)
# draw.polygon(((200, 200), (300, 100), (250, 50)), fill=(255, 255, 0), outline=(0, 0, 0))
# draw.point(((350, 200), (450, 100), (400, 50)), fill=(255, 255, 0))
# im.show()

# draw.ellipse((100, 100, 150, 200), fill=(255, 0, 0), outline=(0, 0, 0))
# draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
# im.show()

draw.arc((25, 50, 175, 200), start=0, end=270, fill=(255, 255, 0))
draw.chord((225, 50, 375, 200), start=30, end=270, fill=(255, 255, 0), outline=(0, 0, 0))
draw.pieslice((425, 50, 575, 200), start=30, end=270, fill=(255, 255, 0), outline=(0, 0, 0))
im.show()
