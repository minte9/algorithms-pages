""" Kock snowflake
You can continue to create new bump (kock curves) foreaver.
Our programs though stops when they get smaller than a few pixels.

A Kock snowflake is three Kock curves in a triangle.
Some of interior lines remains because of small rounding errors. 
"""

import turtle
turtle.tracer(1000, 0)
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()
turtle.pensize(2)

COLOR = 'black'
def drawCurve(start, direction, len, len_limit):

    if len < len_limit: # Base case
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
    turtle.pencolor(COLOR)
    
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
        drawCurve(points[i]['position'], points[i]['direction'], len/3, len_limit)

    

def drawSnowflake(start, direction, len, len_limit=120):

    turtle.penup()
    turtle.goto(start)
    turtle.setheading(direction)

    for i in range(3):
        curveStartPosition = turtle.position()
        curveStartHeading = turtle.heading()

        drawCurve(curveStartPosition, curveStartHeading, len, len_limit)

        # Move back to start position
        turtle.penup()
        turtle.goto(curveStartPosition)
        turtle.setheading(curveStartHeading)

        # Move forward for next side
        turtle.forward(len)
        turtle.right(120)
    

COLOR = 'red'
drawSnowflake((150, 500), 0, 360, 120)

COLOR = 'green'
drawSnowflake((220, 460), 0, 220, 10)

COLOR = 'blue'
drawSnowflake((270, 430), 0, 120, 1)


turtle.exitonclick()