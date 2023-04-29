""" Hilbert curve (1891)
Is a continous fractal space-filling curve.
"""

import turtle
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()
turtle.penup()
turtle.goto((200, 200))
turtle.pendown()

def hilbert_quadrant():
    turtle.left(90);  turtle.forward(50) # Line 1
    turtle.right(90); turtle.forward(50) # Line 2
    turtle.right(90); turtle.forward(50) # Line 3

hilbert_quadrant()
turtle.exitonclick()
