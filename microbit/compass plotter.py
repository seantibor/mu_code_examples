from microbit import *

# get microbit code

while True:  # start infinite loop
    print((compass.heading(), 0))  # write compass heading to the screen
    sleep(50)  # wait for 50 microseconds
