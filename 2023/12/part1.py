"""
"""

import re
from collections import OrderedDict
from functools import reduce
from itertools import combinations, combinations_with_replacement, filterfalse, permutations

lines = []

with open("./12/input.txt") as f:
    for line in f.readlines():
        record = {}
        spring = line.split(" ")[0]
        spring = re.sub("\.+", ".", spring)
        spring = re.sub("^\.+", "", spring)
        spring = re.sub("\.+$", "", spring)
        record["spring"] = spring
        record["data"] = [int(x) for x in line.split(" ")[1].split(",")]
        lines.append(record)

def find_substring(string, l):
    substrings = []
    for i in range(0, len(string) - l + 1):
        sub = string[i:i + l]
        # if not "?" in sub:
        #     continue
        if "." in sub:
            continue
        substrings.append((sub, i, i+l))
    return substrings


def solutions(spring, data, index):
    all_solutions = []
    s = "#" * data[index]
    r = "(?=[#\?]){" + str(data[index]) + "}"
    for sub, start, end in find_substring(spring, data[index]): #re.finditer(r, spring):
        # print(spring, sub, start, end)
        if (start, end) == (0, 0):
            continue
        new_spring = spring[:start] + s + spring[end:]
        if index + 1 < len(data):
            all_solutions.extend(solutions(new_spring, data, index + 1))
        else :
            all_solutions.append(new_spring.replace("?", "."))
    return all_solutions

def all_solutions(springs, data):
    sorted_data = sorted(data, reverse = True)

    # while :


    all_solutions = solutions(springs, sorted_data, 0)
    return all_solutions    


def is_solution_ok(spring, data):
    m = re.finditer("#+", spring)
    newdata = [len(i[0]) for i in m]
    return data == newdata
    

s = 0
i = 0

for l in lines:
    print(i, len(lines))
    locals = 0
    for sol in set(all_solutions(l["spring"], l["data"])):
        # print(sol)
        if is_solution_ok(sol, l["data"]):
            # print(sol, "OK")
            locals +=1
    print(l, locals)
    s += locals
    i += 1


print(s)

