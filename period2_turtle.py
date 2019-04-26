import turtle as t

t.speed(0)

number_of_sides = 6
side_length = 10
complete_rotation = 360
number_of_shapes = 66
t.pencolor((0,0,0))
t.bgcolor('black')

for j in range(number_of_shapes):
    for i in range(number_of_sides):
        t.forward(side_length)
        t.right(complete_rotation/number_of_sides)
    t.circle(side_length / 2)
    t.left(complete_rotation/number_of_shapes + j)
    t.pencolor(0,j / number_of_shapes,0)
    t.forward(5)