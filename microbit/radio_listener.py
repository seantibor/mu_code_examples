from microbit import *
import radio

radio.on()
radio.config(group=1)
print('radio on')

while True:
    msg = radio.receive()
    if msg:
        print(msg)
