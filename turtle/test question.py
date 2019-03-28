import turtle as t
t.pencolor('green')
t.penup()

for x in range(-100, 100):
    y = -6 * x + 21
    t.goto(x, y)
    t.pendown()
