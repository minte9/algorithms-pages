""" Turtle
Turtle graphics were a feature of the Logo programming language,
designed to help kids learn programming.
The feature has been reproduced in ohter languges, including Pyhon.

Lines are displayed on the screen immeaditely.
However, this can slow down programs that draw thousands of line.

With turtle.tracer(1, 0) we can hold on the display, until the line is created.
This example is not a fractal, still, it is a beautiful drawing.

https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md
"""

import turtle
turtle.tracer(1, 0)
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

for i in range(300):
    turtle.pencolor(colors[i%6])
    turtle.forward(i) # distance
    turtle.left(59)   # angle
    print("Distance:", i, "/ Angle: 59")

turtle.exitonclick() # wait for user to close the window