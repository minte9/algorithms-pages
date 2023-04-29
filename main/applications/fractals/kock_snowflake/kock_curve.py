""" Kock curve
A kock curve is composed by three line bumps
VsCode break point on line 50 to debug
"""

import turtle
#turtle.tracer(3, 0)
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()
turtle.pensize(2)

def drawCurve(start, direction, len):

    if len < 120: # Base case
        return 

    points = []

    # Move to start position
    turtle.penup()
    turtle.goto(start)
    turtle.setheading(direction)
    points.append({'position': turtle.position(), 'direction': turtle.heading()})
    
    # Draw initial line
    turtle.pendown()
    turtle.forward(len) # # line 1 (full lenght)

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
    points.append({'position': turtle.position(), 'direction': turtle.heading()})
    turtle.forward(len/3) # middle line 1

    turtle.right(120)
    points.append({'position': turtle.position(), 'direction': turtle.heading()})
    turtle.forward(len/3) # middle line 1

    turtle.left(60)
    points.append({'position': turtle.position(), 'direction': turtle.heading()})

    for i in range(4):
        drawCurve(points[i]['position'], points[i]['direction'], len/3)

drawCurve((200, 300), 0, 360)
turtle.exitonclick()