from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image('90909:09090:90909:09090:90909'))
        sleep(500)
        display.show(Image('09090:90909:09090:90909:09090'))
        sleep(500)
    elif button_b.is_pressed():
        #do something here
        pass
    else:
        display.clear()