# load the turtle library for drawing.
import turtle as t
from itertools import cycle
import random

# make our line thicker
#t.pensize(2)
# make the turtle move faster
t.speed('fastest')
t.shape('turtle')
t.colormode(255)

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'violet'])


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 85:
        return (int(pos * 3), int(255 - (pos * 3)), 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - (pos * 3)), 0, int(pos * 3))
    else:
        pos -= 170
        return (0, int(pos * 3), int(255 - pos * 3))


points = 5
num_shapes = 50
t.penup()
t.goto(-100,240)
t.pendown()

for j in range(num_shapes,0,-1):
    t.fillcolor(wheel(int((j / num_shapes) * 255)))
    # start our square loop
    t.begin_fill()
    for i in range(points):
        t.forward(j * 2)
        t.right(720 / points)
        t.forward(j * 2)
        t.left(360 / points)
    t.end_fill()
    t.right(360 / num_shapes)
    t.forward(j//2)
    new_color = wheel(j)
t.ht()