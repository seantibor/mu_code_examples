from microbit import *
import speech

while True:
    if button_a.was_pressed():
        speech.say('I love the microbit')
