import turtle as t

t.speed(2)

number_of_sides = 300

for i in range(number_of_sides):
    t.forward(100)
    t.left(360/number_of_sides)