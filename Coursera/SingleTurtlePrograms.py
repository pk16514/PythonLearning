# # Program-1


# import turtle             # allows us to use the turtles library

# wn = turtle.Screen()      # creates a graphics window

# alex = turtle.Turtle()    # create a turtle named alex
# alex.forward(150)         # tell alex to move forward by 150 units
# alex.left(90)             # turn by 90 degrees
# alex.forward(75)          # complete the second side of a rectangle

# wn.exitonclick()

# # Program-2


# import turtle

# wn = turtle.Screen()
# wn.bgcolor("green")        # set the window background color

# tess = turtle.Turtle()
# tess.color("blue")              # make tess blue
# tess.pensize(10)                 # set the width of her pen

# tess.forward(50)
# tess.left(120)
# tess.forward(50)

# wn.exitonclick()                # wait for a user click on the canvas

# # Program-3


# """
# The following program uses a turtle to draw a capital L in white on a
# blue background as shown to the left, image of a navigational compass
# and a letter L drawn by Turtle. but the lines are mixed up. The program
# should do all necessary set-up and create the turtle and set the pen size
# to 10. The turtle should then turn to face south, draw a line that is 150
# pixels long, turn to face east, and draw a line that is 75 pixels long.
# Finally, set the window to close when the user clicks in it.
# """

# import turtle

# wn = turtle.Screen()
# wn.bgcolor('blue')

# jamal= turtle.Turtle()
# jamal.color('white')
# jamal.pensize(10)

# jamal.right(90)
# jamal.forward(150)
# jamal.left(90)
# jamal.forward(75)

# wn.exitonclick()

# Program-4


"""
The following program uses a turtle to draw a capital T in white on a green
background as shown to the left, image of a letter T drawn by Turtle. but the
lines are mixed up. The program should do all necessary set-up, create the
turtle, and set the pen size to 10. After that the turtle should turn to face
north, draw a line that is 150 pixels long, turn to face west, and draw a line
that is 50 pixels long. Next, the turtle should turn 180 degrees and draw a
line that is 100 pixels long. Finally, set the window to close when the user
clicks in it.
"""


import turtle

wn = turtle.Screen()
wn.bgcolor('green')

ross = turtle.Turtle()
ross.color('white')
ross.pensize(10)

ross.left(90)
ross.forward(150)
ross.left(90)
ross.forward(50)
ross.right(180)
ross.forward(100)

wn.exitonclick()
