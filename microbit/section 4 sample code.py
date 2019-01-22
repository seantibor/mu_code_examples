# import my microbit information
from microbit import *

i = 0
while i < 5:
    display.clear()
    display.set_pixel(i, 0, 8)
    sleep(500)
    i = i + 1

'''
while True:
    for y in range(5):
        for x in range(5):
            display.clear()
            display.set_pixel(y,x,8)
            sleep(500)
            
'''
