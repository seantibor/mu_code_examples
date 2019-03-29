import time

import analogio
import board
import neopixel
from time import monotonic

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1.0)
light = analogio.AnalogIn(board.LIGHT)

# Turn only pixel #1 green
pixels[1] = (0, 255, 0)

# How many light readings per sample
NUM_OVERSAMPLE = 10
# How many samples we take to calculate 'average'
NUM_SAMPLES = 20
SAMPLE_HZ = 20.0
HISTORY_SECONDS = 2
NUM_HISTORY = HISTORY_SECONDS * int(SAMPLE_HZ)
samples = [0] * NUM_SAMPLES

history = [0] * NUM_HISTORY

def get_bpm(samples):
    beats = 0
    max_sample = max(samples)
    last_sample_was_beat = False
    last_beat_index = None
    beat_times = []
    for i, sample in enumerate(samples):
        if sample > max_sample * 0.60 and not last_sample_was_beat:
            beats += 1
            last_sample_was_beat = True
            if last_beat_index is not None:
                beat_times.append((i - last_beat_index)/SAMPLE_HZ)
            last_beat_index = i
        elif sample < max_sample * 0.50 and last_sample_was_beat:
            last_sample_was_beat = False

    if len(beat_times) > 0:
        bpm_method2 = 60 / (sum(beat_times) / len(beat_times))
    else:
        bpm_method2 = None
    bpm_method1 = beats * (HISTORY_SECONDS / 60)
    return bpm_method1, bpm_method2


last_time = monotonic()
bpm1 = 0
bpm2 = 0
while True:

    for i in range(NUM_SAMPLES):
        if monotonic() > last_time + 1/SAMPLE_HZ:
            last_time = monotonic()
            # Take NUM_OVERSAMPLE number of readings really fast
            oversample = 0
            for s in range(NUM_OVERSAMPLE):
                oversample += float(light.value)
            # and save the average from the oversamples
            samples[i] = oversample / NUM_OVERSAMPLE  # Find the average

            mean = sum(samples) / float(len(samples))  # take the average
            history.insert(0, samples[i]-mean)
            history.pop()
            if samples[i] - mean > .60 * max(history):
                pixels[5] = (255, 0, 255)
            elif samples[i] - mean < .5 * max(history):
                pixels[5] = (0, 0, 0)
            if i == 0:
                bpm1, bpm2 = get_bpm(history)
            pixels.show()
            print((samples[i] - mean, max(history) * 0.6, monotonic() - last_time, bpm1, bpm2))  # 'center' the reading

            #print((bpm1, bpm2))