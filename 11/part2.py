"""
"""

import re
from collections import OrderedDict
from functools import reduce
from itertools import combinations


universe = []
empty_row_index = []

with open("./11/input.txt") as f:
    for line in f.readlines():
        universe.append(list(line.strip()))


# find all the empty rows
for row in range(0, len(universe)):
    if not "#" in universe[row]:
        empty_row_index.append(row)

# find all the empy columns
empty_col_index = []
for col in range(0, len(line)):
    colum = []
    for row in range(0, len(universe)):
        colum.append(universe[row][col])
    if all(list(map(lambda x: x == ".", colum))):
        empty_col_index.append(col)

print(empty_row_index)
print(empty_col_index)
        
# find all galaxy positions
galaxies = []
for row in range(0, len(universe)):
    for col in range(0, len(universe[row])):
        if universe[row][col] == "#":
            galaxies.append((row, col))

print(galaxies)

def number_of_empty_between(rowa, rowb, empty_row_index):
    result = 0
    if rowa > rowb:
        r = rowa
        rowa = rowb
        rowb = r
    for index in empty_row_index:
        if rowa < index and index < rowb:
            result += 1
    return result

def distance(g1, g2):
    distance = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    distance += number_of_empty_between(g1[0], g2[0], empty_row_index) * (1000000 - 1)
    distance += number_of_empty_between(g1[1], g2[1], empty_col_index) * (1000000 - 1)
    return distance

all_pairs = list(combinations(galaxies, 2))
print(len(all_pairs))


s = 0
for p in all_pairs:
    d = distance(p[0], p[1])
    print(p[0], p[1], d)
    s += d

print(s)

            