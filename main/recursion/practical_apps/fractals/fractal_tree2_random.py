""" Fractal Tree - Asymetric
Two branches for every recursive case (left & right)
Difference angles for every recursion turn.
Random seed
"""

import random
import time
import turtle

turtle.tracer(1000, 0)
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()

seed = random.randint(0, 10)
random.seed(seed)

START_LENGTH = 110
ANGLE_L = random.randint(10, 20)
ANGLE_R = random.randint(10, 30)
LENGTH_L = random.randint(8, 15)
LENGTH_R = random.randint(8, 15)

def drawBranch(start, direction, len):
    if len < 5: # Base case
        return 

    # Go to starting point & position
    turtle.penup()
    turtle.goto(start)
    turtle.setheading(direction)

    # Draw the branch (thickness is 1/7 the length)
    turtle.pendown()
    turtle.pensize(max(len/7, 1))
    turtle.forward(len)

    # Record the position of the branch's end
    end = turtle.position()
    
    # Recursive case
    drawBranch(end, direction + ANGLE_L, len - LENGTH_L) # Left Branch
    drawBranch(end, direction - ANGLE_R, len - LENGTH_R) # Right Branch

# Write out the seed number
turtle.penup()
turtle.goto(10, 10)
turtle.write('Random Seed: %s' % (seed))

# Draw the tree
drawBranch((350, 10), 90, START_LENGTH)
turtle.exitonclick()