""" Sierpinsky carpet Fractal
We can draw using rectangles insteed.
"""

import turtle
turtle.tracer(100, 0)
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()

MIN_SIZE = 5 # decrease/increase amount of recursion

def drawCarpet(x, y, width, height): # Outer rectangle
    turtle.penup() # lift up the pen
    turtle.goto(x, y)

    # Draw outer rectangle (carpet)
    turtle.fillcolor("lightblue")
    turtle.begin_fill()
    turtle.pendown()  
    turtle.goto(x, y + height)          # 1st line
    turtle.goto(x + width, y + height)  # 2nd line
    turtle.goto(x + width, y)           # 3td line
    turtle.goto(x, y)                   # 4th line
    turtle.penup()
    turtle.end_fill()

    drawInnerRectangles(x, y, width, height)

def drawInnerRectangles(x, y, width, height): # 9 inner rectables
    if width < MIN_SIZE or height < MIN_SIZE: # Base case
        return

    w = width/3
    h = height/3
    turtle.penup()
    turtle.goto(x + w, y + h)

    # Inner rectangle (center)
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.pendown()
    turtle.goto(x + w,   y + h*2)   # 1st line
    turtle.goto(x + w*2, y + h*2)   # 2nd line
    turtle.goto(x + w*2, y + h)     # 3td line
    turtle.goto(x + w,   y + h)     # 4th line
    turtle.penup()
    turtle.end_fill()

    # Inner rectangles (top)
    drawInnerRectangles(x,       y + 2*h, w, h)
    drawInnerRectangles(x + w,   y + 2*h, w, h)
    drawInnerRectangles(x + 2*w, y + 2*h, w, h)

    # Inner rectangles (middle)
    drawInnerRectangles(x,       y + h, w, h) # left
    drawInnerRectangles(x + w*2, y + h, w, h) # right
    
    # Inner rectangles (bottom)
    drawInnerRectangles(x,       y, w, h)
    drawInnerRectangles(x + w,   y, w, h)
    drawInnerRectangles(x + w*2, y, w, h)

drawCarpet(50, 50, 600, 600)

turtle.exitonclick()