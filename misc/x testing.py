import time
import math
x = 0
sum_circles = 0
pi = 3.14159265

while x < 1000000:
    x += 1
    sum_circles += pi * x ** 2

print(sum_circles)