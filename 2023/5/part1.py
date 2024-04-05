"""
"""

import re
from collections import OrderedDict

maps = OrderedDict()
map_name = ""

def is_seed_in_range_start(s, r):
    if r[1] <= s and s <= r[1] + r[2]:
        return True
    return False

def find_seed_range(s, ranges):
    for r in ranges:
        if is_seed_in_range_start(s, r):
            return r
    return None

def find_seed_dest(s, r):
    diff = s - r[1]
    return r[0] + diff



with open("./5/input.txt") as f:
    for line in f.readlines():
        if line.startswith("seeds"):
            seeds = [int(x) for x in line.strip().split(":")[1].split(" ") if x]
            continue
        if "map" in line:
            map_name = line.split(" ")[0]
            maps[map_name] = []
            continue
        if map_name:
            range = [int(x) for x in line.strip().split(" ") if x]
            if range:
                maps[map_name].append(range)

dest = []


for seed in seeds:
    print(f"for seed {seed}:")
    for k, v in maps.items():
        r = find_seed_range(seed, v)
        if not r:
            print(f"could not find range for {seed}")
        else:
            print(f"{seed}")
            seed = find_seed_dest(seed, r)
            print(f"becomes: {seed}")
    print(f"dest = {seed}")
    dest.append(seed)

print(min(dest))

# print(seeds)
# print(maps)