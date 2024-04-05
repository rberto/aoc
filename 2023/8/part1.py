"""
"""

import re
from collections import OrderedDict
from functools import reduce


nodes = {}

with open("./8/input.txt") as f:
    directions = f.readline().strip()
    for line in f.readlines():
        m = re.match(r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)", line)
        if m:
            nodes[m.group(1)] = (m.group(2), m.group(3))
    
print(directions)
print(nodes)

node = "AAA"
nbsteps = 0
i = 0

while node != "ZZZ":
    if directions[i] == "R":
        node = nodes[node][1]
    if directions[i] == "L":
        node = nodes[node][0]
    i += 1
    if i >= len(directions):
        i = 0
    nbsteps += 1

print(nbsteps)