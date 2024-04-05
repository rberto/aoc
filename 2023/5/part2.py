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

# def is_start_of_range_in_another(srange, seed_ranges):
#     for r in seed_ranges:
#         if srange[0] in range(r[0], r[1])
#             return True
#     return False

def get_all_seeds(seed_ranges):
    new_ranges = []
    for start, end in sorted(seed_ranges):
        if not new_ranges:
            new_ranges.append((start, end))
            continue
        if start < new_ranges[-1][1]:
            new_ranges[-1][1] = max(new_ranges[-1][1], end)
            continue
        if start > new_ranges[-1][1]:
            new_ranges.append((start, end))
            continue
    return new_ranges

seed_ranges = []

with open("./5/input.txt") as f:
    for line in f.readlines():
        if line.startswith("seeds"):
            seeds = [int(x) for x in line.strip().split(":")[1].split(" ") if x]
            for i in range(0, len(seeds), 2):
               seed_ranges.append((seeds[i], seeds[i] + seeds[i+1])) 
            continue
        if "map" in line:
            map_name = line.split(" ")[0]
            maps[map_name] = []
            continue
        if map_name:
            srange = [int(x) for x in line.strip().split(" ") if x]
            if srange:
                maps[map_name].append(srange)


all_ranges = get_all_seeds(seed_ranges)



dest = []
all_seeds = []

for start, end in all_ranges:
    for seed in range(start, end):

        #print(f"for seed {seed}:")
        for k, v in maps.items():
            r = find_seed_range(seed, v)
            if not r:
                #print(f"could not find range for {seed}")
                pass
            else:
                #print(f"{seed}")
                seed = find_seed_dest(seed, r)
                #print(f"becomes: {seed}")
        #print(f"dest = {seed}")
        dest.append(seed)
    print(min(dest))

#print(len(all_seeds))

# print(min(dest))

# print(seeds)
# print(maps)