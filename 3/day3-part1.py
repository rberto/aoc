"""
The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols
 you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be 
 included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right).
 Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""

import re

symbols = ["*", "#", "+", "$", "=", "/"]

def find_numbers(line):
    matches = []
    for m in re.finditer(r"[0-9]+", line):
        matches.append(m)
    return matches

def contains_symbol(line, start, end):
    start = 0 if start < 0 else start
    end = len(line) if end > len(line) else end
    if re.search(r"[^a-zA-Z0-9_\.]", line[start:end]):
        return True
    return False


grid = []

with open("./3/exemple.txt") as f:
    for line in f.readlines():
        grid.append(line.strip())

s = 0

for i in range(0, len(grid)):
    for m in find_numbers(grid[i]):
        cs = contains_symbol(grid[i], m.span()[0] - 1, m.span()[1] + 1)
        if cs: 
            s += int(m.group(0))
            continue
        if i > 0:
            cs = contains_symbol(grid[i-1], m.span()[0] - 1, m.span()[1] + 1)
            if cs: 
                s += int(m.group(0))
                continue
        if i + 1 < len(grid):
            cs = contains_symbol(grid[i+1], m.span()[0] - 1, m.span()[1] + 1)
            if cs: 
                s += int(m.group(0))
                continue

print(s)