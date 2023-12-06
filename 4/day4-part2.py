"""

"""

import re

cards = []

def parseline(line):
    m = re.match(r"Card[ ]+([0-9]+): ([0-9 ]+) ; ([0-9 ]+)$", line)
    return (m.group(1), m.group(2), m.group(3))

def nb_winning_numbers(card):
    return len(list(set(card["win"]) & set(card["draw"])))

def get_from_card_nb(card_nb):
    for c in cards:
        if c["name"] == card_nb:
            return c
    print(f"could not find card nb {card_nb}")
    return None

s = 0

with open("./4/input.txt") as f:
    for line in f.readlines():
        parsed = parseline(line.strip().replace("|", ";"))
        card = {"name": int(parsed[0]),
                    "win": [int(x) for x in parsed[1].strip().split(" ") if x],
                                "draw": [int(x) for x in parsed[2].strip().split(" ") if x]}
        card["nb_of_win_nb"] = nb_winning_numbers(card)
        card["nb_points"] = pow(2, nb_winning_numbers(card) - 1) if nb_winning_numbers(card) > 0 else 0
        card["nb_copy"] = 1
        cards.append(card)


for c in cards: 
    if c['nb_of_win_nb'] > 0:
        for i in range(c["name"] + 1, c["name"] + 1 + c['nb_of_win_nb']):
            get_from_card_nb(i)['nb_copy'] = get_from_card_nb(i)['nb_copy'] + c[('nb_copy')]


for c in cards:
    s += c['nb_copy']

print(s)