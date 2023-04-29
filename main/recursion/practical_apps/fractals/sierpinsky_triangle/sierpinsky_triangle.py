""" Sierpinsky triangle Fractal
The easiest fractal to draw on paper.

Described by polish mathematition in 1915, even using the term fractal.
When you draw the inner equilateral triangle, you form three new triangles.
"""

import turtle
turtle.tracer(100, 0)
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()

MIN_SIZE = 10 # decrease/increase amount of recursion

def midpoint(x1, y1, x2, y2):
    xm = min(x1, x2) + abs(x1 - x2)/2
    ym = min(y1, y2) + abs(y1 - y2)/2
    return (xm, ym) 
        
def drawTriangle(ax, ay, bx, by, cx, cy):
    width = max(ax, bx, cx) - min(ax, bx, cx)
    height = max(ay, by, cy) - min(ay, by, cy)

    # Triangle is to small, stop drawing
    if width < MIN_SIZE or height < MIN_SIZE: # Base case
        return 

    # Draw the triangle
    turtle.penup()      # lift up the pen
    turtle.goto(ax, ay)
    turtle.pendown()    # draw start
    turtle.goto(bx, by) # 1st line
    turtle.goto(cx, cy) # 2nd line
    turtle.goto(ax, ay) # 3th line
    turtle.penup()      # draw stop

    # Calculate midpoints
    abm = midpoint(ax, ay, bx, by)
    bcm = midpoint(bx, by, cx, cy)
    acm = midpoint(cx, cy, ax, ay)

    # Draw innner triangles
    drawTriangle(ax, ay, abm[0], abm[1], acm[0], acm[1])
    drawTriangle(abm[0], abm[1], bx, by, bcm[0], bcm[1])
    drawTriangle(acm[0], acm[1], bcm[0], bcm[1], cx, cy)

drawTriangle(50, 50, 350, 650, 650, 50) # equilateral Siepinsky triangle

#drawTriangle(50, 50, 350, 350, 350, 50) # skewed example

turtle.exitonclick()