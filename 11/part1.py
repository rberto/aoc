"""
"""

import re
from collections import OrderedDict
from functools import reduce
from itertools import combinations


universe = []

with open("./11/input.txt") as f:
    for line in f.readlines():
        universe.append(list(line.strip()))
        if not "#" in line:
            universe.append(list(line.strip()))

empty_col_index = []

for col in range(0, len(line)):
    colum = []
    for row in range(0, len(universe)):
        colum.append(universe[row][col])
    if all(list(map(lambda x: x == ".", colum))):
        empty_col_index.append(col)

print(empty_col_index)

for row in range(0, len(universe)):
    nbinsert = 0
    for index in empty_col_index:
        universe[row].insert(index + nbinsert, ".")
        nbinsert += 1

print(universe)
        
# find all galaxy positions
galaxies = []
for row in range(0, len(universe)):
    for col in range(0, len(universe[row])):
        if universe[row][col] == "#":
            galaxies.append((row, col))

print(galaxies)


def distance(g1, g2):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

all_pairs = list(combinations(galaxies, 2))


s = 0
for p in all_pairs:
    s += distance(p[0], p[1])

print(s)

            