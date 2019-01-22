import board
import busio as io
import adafruit_ssd1306
from digitalio import DigitalInOut, Direction, Pull
from random import choice
from time import sleep

# initialize I2C with default pins
i2c = io.I2C(board.SCL, board.SDA)

reset_pin = DigitalInOut(board.D12)
change_msg_pin = DigitalInOut(board.D9)
change_msg_pin.direction = Direction.INPUT
change_msg_pin.pull = Pull.DOWN

# initialize the OLED display
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, reset=reset_pin)
messages = ['You go, girl!', 'Sister Slamming', 'You are\nbeautiful and\nso loved', 'You are so\nfresh']


def print_message(message):
    oled.fill(0)
    words = message.splitlines()
    line_num = 0
    for word in words:
        oled.text(word.center(16), 0, line_num * 10)
        line_num += 1
    oled.show()


while True:
    print(change_msg_pin.value)
    if change_msg_pin.value and not pin_state:
        print_message(choice(messages))
        pin_state = True
    else:
        pin_state = False
    sleep(0.1)
