"""
"""

import re
from collections import OrderedDict
from functools import reduce


nodes = {}

with open("./8/input.txt") as f:
    directions = f.readline().strip()
    for line in f.readlines():
        m = re.match(r"([0-9A-Z]+) = \(([0-9A-Z]+), ([0-9A-Z]+)\)", line)
        if m:
            nodes[m.group(1)] = (m.group(2), m.group(3))
    
#print(directions)
#print(nodes)

starting_nodes = []

for key in nodes.keys():
    if key.endswith("A"):
        starting_nodes.append(key)

#starting_nodes = starting_nodes[2:4]

print(starting_nodes)

def step(node_dir):
    node, direction = node_dir
    if direction == "R":
        result = nodes[node][1]
    if direction == "L":
        result = nodes[node][0]
    return result

i = 0
nbsteps = 0

while not all(map(lambda x: x.endswith("Z"), starting_nodes)):
    starting_nodes = list(map(step, [(x, directions[i]) for x in starting_nodes]))
    i += 1
    if i >= len(directions):
        i = 0
    nbsteps += 1


    
print(starting_nodes)
print(nbsteps)