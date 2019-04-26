from microbit import *
import radio

radio.on()

while True:
    if button_a.is_pressed():
        for x in range(5):
            for y in range(5):
                display.show(Image('9999:' * 5))
                sleep(30)
                display.clear()
    elif button_b.is_pressed():
        display.show(Image('12345:23456:34567:45678:56789'))
    else:
        display.clear()