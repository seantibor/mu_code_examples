from microbit import *

compass.calibrate()

while True:
    needle = ((15 - compass.heading() - 7) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])
    sleep(1)
    if button_a.was_pressed():
        display.scroll(compass.heading())