import turtle


# # Program-1


# """
# The following program uses the stamp method to create a circle of turtle
# shapes as shown to the left, image of a circle of turtle shapes but the
# lines are mixed up. The program should do all necessary set-up, create the
# turtle, set the shape to "turtle", and pick up the pen. Then the turtle
# should repeat the following ten times: go forward 50 pixels, leave a copy of
# the turtle at the current position, reverse for 50 pixels, and then turn
# right 36 degrees. After the loop, set the window to close when the user
# clicks in it.
# """


# wn = turtle.Screen()

# tess = turtle.Turtle()
# tess.shape('turtle')
# tess.speed(1)
# tess.up()

# for i in range(10):
#     tess.color('blue')
#     tess.forward(50)
#     tess.stamp()
#     tess.forward(-50)
#     tess.right(36)
# tess.color('red')

# wn.exitonclick()

# Program-2


wn = turtle.Screen()

tess = turtle.Turtle()
tess.shape('turtle')
tess.color('blue')
tess.speed(0)
tess.up()
dist = 10
angle = 55

for i in range(1000):
    tess.stamp()
    tess.left(angle)
    tess.forward(dist)
    dist += 2

wn.exitonclick()
