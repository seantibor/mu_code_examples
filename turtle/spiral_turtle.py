import turtle as t

t.penup()
t.goto(200,0)
t.pendown()

for i in range(360):
    t.forward(i//6 if i < 180 else (360-i)//6)
    t.left(90-0.5*i)