import turtle


# Program-1


"""
The following program has one turtle, "jamal", draw a capital L in blue
and then another, "tina", draw a line to the west in orange as shown to
the left, image of a capital letter L in blue color drawn by one Turtle
and a line to the west in orange color drawn by another Turtle. Both the
Turtles have same starting point.. The program should do all set-up, have
"jamal" draw the L, and then have "tina" draw the line. Finally, it should
set the window to close when the user clicks in it. Make pensize of both 10.
"""


wn = turtle.Screen()

jamal = turtle.Turtle()
jamal.color('blue')
jamal.pensize(10)

jamal.right(90)
jamal.forward(150)
jamal.left(90)
jamal.forward(75)

tina = turtle.Turtle()
tina.color('orange')
tina.pensize(10)

tina.left(180)
tina.forward(75)

wn.exitonclick()

# Program-2


wn = turtle.Screen()

tess = turtle.Turtle()
tess.color('hotpink')
tess.pensize(3)


distance = 150
for i in range(13):
    tess.left(120)
    tess.forward(distance)
    distance += 10

wn.exitonclick()

# Program-3


"""
Note- 1. Every turtle can have its own shape. The ones available “out of the
         box” are arrow, blank, circle, classic, square, triangle, turtle.

      2. You can speed up or slow down the turtle’s animation speed. (Animation
         controls how quickly the turtle turns and moves forward). Speed
         settings can be set between 1 (slowest) to 10 (fastest). But if you
         set the speed to 0, it has a special meaning — turn off animation and
         go as fast as possible.

      3. A turtle can “stamp” its footprint onto the canvas, and this will
         remain after the turtle has moved somewhere else. Stamping works even
         when the pen is up.
"""


wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue", "yellow")           # .color(pencolor, shapecolor)
tess.shape("turtle")
tess.speed(0)

dist = 5
tess.up()                     # this is new
for _ in range(30):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(dist)          # move tess along
    tess.right(24)              # and turn her
    dist = dist + 2
    print(dist)
tess.color('red')

wn.exitonclick()
