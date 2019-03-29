import turtle as t

t.goto(0,0)

t.pencolor('black')
t.penup()

for x in range(-50,51):
    x *= 0.2
    y = x**2
    print((x,y))
    t.goto(x,y)
    t.pendown()