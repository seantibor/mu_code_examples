import turtle as t
from random import choice

num_sides = 7
num_shapes = 100
colors = ['red','yellow', 'blue','green','orange','pink','violet','purple']

t.speed(10**10)
for j in range(num_shapes):
    t.pencolor(choice(colors))
    for i in range(num_sides):
        t.forward(50)
        t.right(360 / num_sides)
    t.left(360/num_shapes)