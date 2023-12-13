"""
"""

import re
from collections import OrderedDict
from functools import reduce


times = []
distance = []

with open("./6/input.txt") as f:
    for line in f.readlines():
        if "Time" in line:
            times = [int(x) for x in line.split(":")[1].split(" ") if x]
        if "Distance" in line:
            distance = [int(x) for x in line.split(":")[1].split(" ") if x]

games = list(zip(times, distance))

print(games)

def distance(speed, time):
    return time * speed

def time(maxt, button):
    return maxt - button

def d(button, maxt):
    return distance(button, time(maxt, button))

result = []

for maxt, record in games:
    result.append(0)
    for button in range(1, maxt):
        if d(button, maxt) > record:
            result[-1] += 1

print(result)

print(reduce(lambda x, y: x*y, result))