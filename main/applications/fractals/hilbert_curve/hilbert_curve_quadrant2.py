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

LENGTH = 50

def hilbert_quadrant(angle, level):    
    if level == 0: # Base case
        return 

    turtle.left(angle)
    hilbert_quadrant(-angle, level-1)

    turtle.pencolor('red' if level == 2 else 'black') # connect line
    turtle.forward(LENGTH) 

    turtle.right(angle)
    hilbert_quadrant(angle, level-1)

    turtle.pencolor('red' if level == 2 else 'black') # connect line
    turtle.forward(LENGTH)

    hilbert_quadrant(angle, level-1)
    turtle.right(angle)

    turtle.pencolor('red' if level == 2 else 'black') # connect line
    turtle.forward(LENGTH)

    hilbert_quadrant(-angle, level-1)
    turtle.left(angle)
    return

hilbert_quadrant(90, 2)
turtle.exitonclick()
