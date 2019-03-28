import time
import math
from adafruit_circuitplayground.express import cpx
from itertools import cycle
 

notes = {
  'g': 392,
  'a': 440,
  'b': 494,
  'c': 262,
}

line1 = ['g:4', 'a:4', 'b:4', 'c:4']
line2 = ['c:8', 'c:8', 'gc8']
frere_jaques = cycle(line1 + line2)


def play(note):
    name, duration = note.split(':')
    cpx.play_tone(notes[name], duration/10)

 
while True:
    x, y, z = cpx.acceleration
    time.sleep(0.1)
    acceleration_vector = math.sqrt(x**2 + y**2 + z**2)
    print((acceleration_vector,))
    
    if acceleration_vector > 10:
        cpx.pixels.fill((0, 0, 255))
        play(next(frere_jaques))
    else:
        cpx.pixels.fill((0, 0, 0))
    cpx.pixels.show()