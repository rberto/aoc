"""
"""

import re
from collections import OrderedDict
from functools import reduce

grid = []

i = 0
startx = 0
starty = 0

Sequivalent = "7"

pieces = {"-": [(0,1), (0,-1)], 
 "|": [(1,0), (-1,0)],
 "L": [(0,1), (-1,0)],
 "J": [(0,-1), (-1,0)],
 "F": [(0,1), (1,0)],
 "7": [(0,-1), (1,0)]}

with open("./10/input.txt") as f:
    for line in f.readlines():
        if "S" in line:
            startx = i
            starty = line.index("S")
            line = line.replace("S", Sequivalent)
        grid.append(line.strip())
        
        i += 1

print(grid, startx, starty)

def get_next_position(previous, position):
    newposition = tuple(map(sum, zip(position, pieces[grid[position[0]][position[1]]][0])))
    if newposition == previous:
        newposition = tuple(map(sum, zip(position, pieces[grid[position[0]][position[1]]][1])))
    return newposition

previous = (startx, starty)
position = (startx + 1, starty)

j = 0

while position != (startx, starty):
    new_position = get_next_position(previous, position)
    previous = position
    position = new_position
    j += 1

j = j +1
print(j/2)