# bring in all my microbit functions and libraries
from microbit import *

while True:
    if accelerometer.was_gesture('shake'):
        for x in range(5):
            display.clear()  # turn off all the lights
            display.set_pixel(x, 0, 8)  # turn just one light on
            sleep(100)  # slow down the loop
    if button_b.was_pressed():
        display.clear()
        current_temp = temperature()
        display.scroll(str(current_temp) + " C")
'''
while True:  #outer loop that runs forever
    for y in range(5):  #loop that moves to the next line of leds
        for x in range(5):  #loop that moves the led from left to right
            display.clear()  #turn off all the lights
            display.set_pixel(x, y, 8)  #turn just one light on
            sleep(100)  #slow down the loop
'''
