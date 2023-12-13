"""
"""

import re
from collections import OrderedDict
from functools import reduce


with open("./6/input.txt") as f:
    for line in f.readlines():
        if "Time" in line:
            times = int(line.replace(" ", "").split(":")[1].strip())
        if "Distance" in line:
            record = int(line.replace(" ", "").split(":")[1].strip())

print(times, record)

def distance(speed, time):
    return time * speed

def t(maxt, button):
    return maxt - button

def d(button, maxt):
    return distance(button, t(maxt, button))

result = 0

for button in range(1, times):
    if d(button, times) > record:
        result += 1

print(result)
