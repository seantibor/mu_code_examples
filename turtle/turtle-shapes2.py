import turtle as t
from random import choice

t.pencolor('red')
t.speed('slow')
num_sides = 7
num_shapes = 100

for j in range(num_shapes):
    for i in range(num_sides):
        t.pencolor(choice(('red','blue','purple')))
        t.forward(100)
        t.right(360/num_sides)
    t.right(360/num_shapes)