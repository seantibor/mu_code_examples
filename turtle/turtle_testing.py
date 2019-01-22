# load the turtle library for drawing.
import turtle as t
import random
from itertools import cycle

# make our line thicker
t.pensize(2)
# make the turtle move faster
t.speed('fastest')
# change the shape of the cursor to be a turtle
t.shape('turtle')

# variables to track number of sides and shapes to be drawn
sides = 5
num_shapes = 200
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'violet'])

for y in range(num_shapes):
    t.pencolor(next(colors))
    # start our shape loop
    for i in range(sides):
        t.forward(100)
        t.right(360 / sides)
    t.left(360 / num_shapes)
