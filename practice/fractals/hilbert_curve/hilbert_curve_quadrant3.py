""" Hilbert curve (1891)
Is a continuous fractal space-filling curve.
"""

import turtle
turtle.tracer(1, 0)
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()
turtle.penup()
turtle.goto((200, 400))
turtle.pendown()

LENGTH = 30
COLORS = ['black', 'red', 'orange']

def hilbert_quadrant(angle, level):    
    if level == 0: # Base case
        return 

    turtle.left(angle)
    hilbert_quadrant(-angle, level-1)

    turtle.pencolor(COLORS[level-1]) # connect line
    turtle.forward(LENGTH) 

    turtle.right(angle)
    hilbert_quadrant(angle, level-1)

    turtle.pencolor(COLORS[level-1]) # connect line
    turtle.forward(LENGTH)

    hilbert_quadrant(angle, level-1)
    turtle.right(angle)

    turtle.pencolor(COLORS[level-1]) # connect line
    turtle.forward(LENGTH)

    hilbert_quadrant(-angle, level-1)
    turtle.left(angle)
    return

hilbert_quadrant(90, 3)
turtle.exitonclick()
