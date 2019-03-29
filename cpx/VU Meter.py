# import necessary libraries
import board
import math
import time
from analogio import AnalogIn
from adafruit_circuitplayground.express import cpx

N_PIXELS = 150
MIC_PIN = 1
LED_PIN = 10
SAMPLE_WINDOW = 10
PEAK_HANG = 24
PEAK_FALL = 4
INPUT_FLOOR = 10
INPUT_CEILING = 300

# Exponential scaling factor.
# Should probably be in range -10 .. 10 to be reasonable.
CURVE = 2
SCALE_EXPONENT = math.pow(10, CURVE * -0.1)

peak = 16  # peak level of column; used for falling dots
sample = 0
dotCount = 0  # frame counter for peak dot
dotHangCount = 0  # frame counter for holding peak dot

# set the brightness of the leds
pixelBrightness = 0.3

cpx.pixels.brightness = pixelBrightness
analog_in = AnalogIn(board.A1)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)
    if pos < 85:
        return (int(255 - pos*3), int(pos*3), 0)
    elif pos < 170:
        pos -= 85
        return (0, int(255 - (pos*3)), int(pos*3))
    else:
        pos -= 170
    return (int(pos*3), 0, int(255 - pos*3))

def log_scale(input_value, input_min, input_max, output_min, output_max):
    normalized_input_value = (input_value - input_min) / \
                             (input_max - input_min)
    return output_min + \
        math.pow(normalized_input_value, SCALE_EXPONENT) \
        * (output_max - output_min)

def get_sample(pin):
    return pin.value * 1023 / 65536

while True:
    startMillis = int(round(time.time() * 1000))
    peakToPeak = 0.0
    signalMax = 0
    signalMin = 1023
    c = 0
    y = 0

    while round(time.time() * 1000) - startMillis < SAMPLE_WINDOW:
        sample = get_sample(analog_in)
        if sample < 1024:
            if sample > signalMax:
                signalMax = sample
            elif sample < signalMin:
                signalMin = sample
    peakToPeak = signalMax - signalMin
    for i in range(N_PIXELS - 1):
        cpx.pixels[i] = wheel(i * 120 / N_PIXELS-1 + 30)
    log_scale(peakToPeak, INPUT_FLOOR, INPUT_CEILING, N_PIXELS, 0)
    if c < peak:
        peak = c
        dotHangCount = 0
    if c <= N_PIXELS:
        for i in range(N_PIXELS-c, N_PIXELS, 1):
            cpx.pixels[i] = ((0, 0, 0))
    y = N_PIXELS - peak
    cpx.pixels[y-1] = wheel(i * 120 / N_PIXELS-1 + 30)
    cpx.pixels.show()
    if dotHangCount > PEAK_HANG:
        if ++dotCount >= PEAK_FALL:
            peak += 1
            dotCount = 0
    else:
        dotHangCount += 1
