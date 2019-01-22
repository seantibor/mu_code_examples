# you have to put it into mu to make it work

from tkinter import *
import random
import time


# create an initialization function
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        # create list with six numbers
        starts = [-3, -2, -1, 1, 2, 3]
        # mix up list of numbers
        random.shuffle(starts)
        self.x = starts[0]
        # speed up the ball
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        # create cordinates for the top of the ball
        if pos[1] <= 0:
            self.y = 3
        # create cordinates for bottom of the ball
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.y = 3
        if pos[2] >= self.canvas_height:
            self.y = -3


# create the gaming canvas
tk = Tk()
tk.title("Game")
# show that the size of the window cannot be changed either horizontally or vertically
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

# create a purple ball object
ball = Ball(canvas, 'purple')

while 1:
    # draw function
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
