import time
import turtle as t
from random import randint

x = 0
t.speed(0)
t.colormode(255)

while x < 1000:
    t.color((abs(x%255 - 127),0,255-abs(x%255 - 127)))
    x += 1
    t.circle(x,120)
    t.forward(2)
    t.left(2)