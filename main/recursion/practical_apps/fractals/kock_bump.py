""" Kock bump
Measuring an island coast more precisely adds to the length.
Kock curve (1902) is one of the earliest fractals described mathematically.
To construct it, take a line and divid it into three equal parts.

Replace the middle part with a bump.
This cause the Koch curve to be longer than the original line.
Each time we create a bump the length increases from three b/3 to four. 
"""

import turtle
# turtle.tracer(10, 0)
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()
turtle.pensize(2)

def drawCurve(start, direction, len):

    # Move to start position
    turtle.penup()
    turtle.goto(start)
    turtle.setheading(direction)
    
    # Draw initial line
    turtle.pendown()
    turtle.forward(len) # line 1 (full lenght)

    # Erase the middle third line
    turtle.backward(2 * len/3)
    turtle.pencolor('white')
    turtle.forward(len/3)

    # Move to bump position
    turtle.penup()
    turtle.backward(len/3)
    turtle.pendown()
    turtle.pencolor('black')

    # Draw the bump
    turtle.left(60)
    turtle.forward(len/3) # middle line 1
    turtle.right(120)
    turtle.forward(len/3) # middle line 2

drawCurve((200, 300), 0, 300)
turtle.exitonclick()