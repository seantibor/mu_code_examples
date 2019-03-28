import turtle as t

t.speed('fastest')

num_sides = 5
num_shapes = 50

for j in range(num_shapes):
    for i in range(num_sides):
        t.forward(60)
        t.left(720/num_sides)
        t.forward(60)
        t.right(360/num_sides)
    t.right(360/num_shapes)
