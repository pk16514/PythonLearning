import random
import turtle


def stillIn():
    if random.random() > 0.1:
        return True
    else:
        return False


wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape('turtle')

while stillIn():
    coin = random.randrange(0, 2)

    if coin == 0:
        alex.left(90)
    else:
        alex.right(90)
    alex.forward(50)

wn.exitonclick()

# Method-2


def stillIn():
    leftbound = -(wn.window_width() / 2)
    rightbound = (wn.window_width() / 2)
    topbound = (wn.window_height() / 2)
    bottombound = -(wn.window_height() / 2)

    turtleX = alex.xcor()
    turtleY = alex.ycor()

    stillInside = True

    if turtleX > rightbound or turtleX < leftbound:
        stillInside = False
    if turtleY > topbound or turtleY < bottombound:
        stillInside = False
    return stillInside


wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape('turtle')

while stillIn():
    coin = random.randrange(0, 2)

    if coin == 0:
        alex.left(90)
    else:
        alex.right(90)
    alex.forward(50)

wn.exitonclick()
