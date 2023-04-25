""" Sierpinsky triangle Fractal
The easiest fractal to draw on paper.

Described by polish mathematition in 1915, even using the term fractal.
When you draw the inner equilateral triangle, you form three new triangles.
"""

import turtle
turtle.tracer(50, 0)
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()

MIN_SIZE = 4

def midpoint(startx, starty, endx, endy):
    xDiff = abs(startx - endx)
    yDiff = abs(starty - endy)
    return (min(startx, endx) + (xDiff / 2.0), 
            min(starty, endy) + (yDiff / 2.0))

def drawTriangle(ax, ay, bx, by, cx, cy):

    width = max(ax, bx, cx) - min(ax, bx, cx)
    height = max(ay, by, cy) - min(ay, by, cy)

    # Triangle is to small, stop drawing
    if width < MIN_SIZE or height < MIN_SIZE: # Base case
        return 

    # Draw the triangle
    turtle.penup() # lift up the pen
    turtle.goto(ax, ay)
    turtle.pendown()
    turtle.goto(bx, by)
    turtle.goto(cx, cy)
    turtle.goto(cx, cy)
    turtle.pendown()

    # Calculate midpoints
    abm = midpoint(ax, ay, bx, by)
    bcm = midpoint(bx, by, cx, cy)
    acm = midpoint(cx, cy, ax, ay)

    # Draw innner triangles
    drawTriangle(ax, ay, abm[0], abm[1], acm[0], acm[1])
    drawTriangle(abm[0], abm[1], bx, by, bcm[0], bcm[1])
    drawTriangle(acm[0], acm[1], bcm[0], bcm[1], cx, cy)

drawTriangle(50, 50, 350, 650, 650, 50)

turtle.exitonclick()