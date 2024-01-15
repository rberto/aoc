"""
"""

import re
from collections import OrderedDict
from functools import reduce

lines = []

with open("./9/input.txt") as f:
    for line in f.readlines():
        lines.append([int(x.strip()) for x in line.split(" ") if x])

reversed_lines = []

for line in lines:
    reversed_lines.append(list(reversed(line)))

lines = reversed_lines

print(lines)

def derive(line):
    i = 0
    result = []
    while i < len(line) - 1:
        result.append(line[i+1] - line[i])
        i += 1
    return result

def interpol(a, b):
    b.append(b[-1] + a[-1])
    return b

def interpolate(line):
    steps = []
    steps.append(line)
    while not all(list(map(lambda x: x == 0, steps[-1]))):
        steps.append(derive(steps[-1]))
    steps[-1].append(0)
    i = len(steps) - 1
    while i != 0:
        steps[i-1] = interpol(steps[i], steps[i-1])
        i -= 1
    return steps

s = 0

for line in lines:
    s += interpolate(line)[0][-1]

print(s)