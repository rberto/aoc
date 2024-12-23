"""
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola,
 finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", 
so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer,
 holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. 
 You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong.
 A gear is any * symbol that is adjacent to exactly two part numbers.
  Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear
 needs to be replaced.

Consider the same engine schematic again:

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
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345.
 The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent 
 to one part number.) Adding up all of the gear ratios produces 467835.
"""

import re


def find_numbers(line):
    matches = []
    for m in re.finditer(r"[0-9]+", line):
        matches.append(m)
    return matches

def find_all_stars(line):
    return [x.span()[0] for x in re.finditer(r"[*]", line)]


def contains_star(line, start, end):
    start = 0 if start < 0 else start
    end = len(line) if end > len(line) else end
    if re.search(r"[*]", line[start:end]):
        return True
    return False

def is_near_star(line, m, star):
    start = 0 if m.span()[0] - 1 < 0 else m.span()[0] - 1
    end = len(line) if m.span()[1] > len(line) else m.span()[1]
    if start <= star and star <= end:
        return True
    return False


grid = []

with open("./3/input.txt") as f:
    for line in f.readlines():
        grid.append(line.strip())

s = 0

for i in range(0, len(grid)):

    for star in find_all_stars(grid[i]):
        numbers = []
        if i > 0:
            numbers.extend(find_numbers(grid[i-1]))
        numbers.extend(find_numbers(grid[i]))
        if i < len(grid) - 1:
            numbers.extend(find_numbers(grid[i+1]))
        near_numbers = [x.group(0) for x in numbers if is_near_star(grid[i], x, star)]
        if len(near_numbers) == 2:
            s += int(near_numbers[0]) * int(near_numbers[1])

print(s)