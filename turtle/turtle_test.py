# load the turtle library
import turtle as t
# loading a cycle function
from itertools import cycle


def draw_shape(sides, size, color):
    # shape loop
    t.pencolor(color)
    for i in range(sides):
        # move the turtle forward by the size pixels
        t.forward(size)
        # turn the turtle right a number of degrees based on the number of sides
        t.right(360 / sides)


# define a list of colors
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'violet'])

# speed the turtle up
t.speed('fastest')

num_sides = 8
num_shapes = 60

for y in range(num_shapes):
    # pick my next color from the wheel
    draw_shape(num_sides, 30, next(colors))
    t.left(360 / num_shapes)
