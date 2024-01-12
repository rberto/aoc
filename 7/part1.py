"""
"""

import re
from collections import OrderedDict
from functools import reduce


def key2number(key):
    if key.isdigit():
        return int(key)
    else:
        if key == 'T':
            return 10
        elif key == 'J':
            return 11
        elif key == 'Q':
            return 12
        elif key == 'K':
            return 13
        elif key == 'A':
            return 14

def str2hand(string):
    hand = {}
    for c in string:
        if c not in hand.keys():
            hand[key2number(key)] = string.count(c)
    return hand

def hand_cmp(h1, h2):
    if max(h1.values()) > max(h2.values()):
        return h1
    elif max(h1.values()) == max(h2.values()):
        if max(h1.values()) == 4:
            h3 = dict(h1)
            h3.pop(max(h1.keys()))
            h4 = dict(h2)
            h4.pop(max(h2.keys()))
        
            

def handbid_cmp(hb1, hb2):
    h1 = hb1[0]
    h2 = hb2[0]
    return hand_cmp(h1, h2)

def hand_score(hb):
    h = hb[0]
    score = 0
    for k, v in h.items():
        score += key2number(k) * v
    if max(h.values()) == 5:
        score *= pow(10, 7)
    elif max(h.values()) == 4:
        score *= pow(10, 6)
    elif max(h.values()) == 3 and 2 in h.values():
        score *= pow(10, 5)
    elif max(h.values()) == 3 and 2 not in h.values():
        score *= pow(10, 4)
    elif list(h.values()).count(2) == 2:
        score *= pow(10, 3)
    elif max(h.values()) == 2:
        score *= pow(10, 2)
    elif max(h.values()) == 1:
        score += max([key2number(x) for x in h.keys()])
    return score

    
handsbid = []

with open("./7/exemple.txt") as f:
    for line in f.readlines():
        handsbid.append((str2hand(line.split(" ")[0]), int(line.split(" ")[1])))

print(handsbid)

handsbid.sort(key = hand_score)

print(handsbid)