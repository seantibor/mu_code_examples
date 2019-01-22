from microbit import *

maximum_sample_rate = 50  # samples per second

while True:
    x = accelerometer.get_x() / 1000  # convert from milli-g's to g's
    y = accelerometer.get_y() / 1000
    z = accelerometer.get_z() / 1000
    print((x, y, z))  # print a tuple to the REPL so it can be plotted
    sleep(1000 / maximum_sample_rate)
