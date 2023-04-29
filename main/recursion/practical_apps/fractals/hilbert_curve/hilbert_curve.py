""" Hilbert curve (1891)
Is a continuous fractal space-filling curve.
"""

import turtle
turtle.tracer(10, 0)
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()

ANGLE = 90
LEVEL = 6
LINE_LENGTH = 5

def hilbert_cuadrant(angle, level):    
    if level == 0: # Base case
        return 

    turtle.left(angle)
    hilbert_cuadrant(-angle, level-1)
    turtle.forward(LINE_LENGTH) 

    turtle.right(angle)
    hilbert_cuadrant(angle, level-1)
    turtle.forward(LINE_LENGTH)

    hilbert_cuadrant(angle, level-1)
    turtle.right(angle)
    turtle.forward(LINE_LENGTH)

    hilbert_cuadrant(-angle, level-1)
    turtle.left(angle)
    return

def hilbert_curve(position):
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()
    hilbert_cuadrant(ANGLE, LEVEL)


hilbert_curve((30, 350))        # Upper left quadrant
turtle.forward(LINE_LENGTH)

hilbert_cuadrant(ANGLE, LEVEL)  # Upper right quadrant
turtle.left(3*ANGLE)
turtle.forward(LINE_LENGTH)
turtle.right(ANGLE)

hilbert_cuadrant(ANGLE, LEVEL)  # Lower right quadrant
turtle.left(-4*ANGLE)
turtle.forward(LINE_LENGTH)

hilbert_cuadrant(ANGLE, LEVEL)  # Lower left quadrant
turtle.exitonclick()
