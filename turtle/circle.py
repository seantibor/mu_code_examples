# A growing circle

from matplotlib import pyplot as plt
from matplotlib import animation


def create_circle():
    circle = plt.Circle((0, 0), 0.05)
    return circle


def update_radius(i, circle):
    circle.radius = i * 0.5
    return circle,


def create_animation():
    fig = plt.gcf()
    ax.set_aspect('equal')
    circle = create_circle()
    ax.add_patch(circle)
    anim = animation.funcanimation(
        fig, update_radius, frags=(circle,), frames=30, interval=50)
    plt.title('Simple Circle Animation')
    plt.show()


if _name_ == '_main_':
    create_animation()

import turtle

myTurtle = turtle.Turtle(shape="turtle")
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-120, 0)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(60, 60)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-60, 60)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-180, 60)
myTurtle.pendown()
myTurtle.circle(50)

turtle.getscreen()._root.mainloop()
