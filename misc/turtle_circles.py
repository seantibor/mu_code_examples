import turtle as t
from random import randint

r = 0
t.speed(0)
t.penup()
#t.goto(0, -300)
t.pendown()
t.colormode(255)

def random_color():
    return (0,randint(0,255),0)

while r < 10000:
    r += 1
    t.color(random_color())
    t.circle(r)
    t.forward(1)
    t.left(2)