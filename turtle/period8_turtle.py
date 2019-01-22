# we are using the turtle code library
import turtle as t

# set my pensize to size 2 to make the lines thicker
t.pensize(2)

for j in range(20):
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.right(20)
