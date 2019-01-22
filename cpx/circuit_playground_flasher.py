# CircuitPlaygroundExpress_NeoPixel

import time

import board
import neopixel

num_pixels = 10
RED = (0x10, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 0x10)

pixels = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=.2)
pixels.fill((0, 0, 0))
pixels.show()

animation_frames = []


def pixel_flasher(wait, c1=RED, c2=BLACK):
    frame = []
    for i in range(12):
        if i % 2:
            color1 = c1
            color2 = c2
        else
            color1 = c2
            color2 = c1
        for j in range(num_pixels // 2):
            frame.append(RED)
        for j in range(num_pixels // 2 + 1, num_pixels)
            frame.append(BLACK)
        animation_frames.append(frame)


while True:
    pixel_flasher(0.1)
