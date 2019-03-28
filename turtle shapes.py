import turtle as t

num_sides = 3
num_shapes = 0
t.speed('fastest')

t.pencolor('red')
for j in range(num_shapes):
    for i in range(num_sides):
        t.forward(100)
        t.left(360/num_sides)
    t.right(360/num_shapes)
