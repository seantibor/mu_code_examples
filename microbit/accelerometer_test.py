from microbit import *

while True:
    x_value = accelerometer.get_x()
    y_value = accelerometer.get_y()
    x_value = (x_value * 100) // 1023
    y_value = (y_value * 100) // 1023
    # begin controlled section
    x_value //= 2
    y_value //= 2
    left = y_value - x_value
    right = y_value + x_value
    print((x_value, y_value, left, right))
    sleep(100)
