import turtle as t
from random import choice
import itertools as it

num_sides = 20
num_shapes = 20
t.speed('fastest')
colors = it.cycle(('red','orange','yellow','green','blue','purple','violet'))


# this draws all the shapes
for j in range(num_shapes):
    # this draws one shape
    t.fillcolor(next(colors))
    t.begin_fill()
    for i in range(num_sides):
        t.forward(50)
        t.right(360/num_sides)
    # this moves a little bit between shapes
    t.end_fill()
    t.left(360/num_shapes)
    #t.forward(5)