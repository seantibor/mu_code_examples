# we are using the turtle code library
import turtle as t
from random import randint

num_sides = int(input("how many sides? "))
num_shapes = 100
my_color = input("what color? ")

# set my pensize to size 2 to make the lines thicker
t.pensize(2)
t.speed(0)
t.pencolor(my_color)

for j in range(num_shapes):
    for i in range(num_sides):
        t.forward(30)
        t.right(360/num_sides)
    t.penup()
    t.goto(randint(-400,400),randint(-400,400))
    t.pendown()