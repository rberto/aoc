"""

"""

import re

cards = []
cards.append({})

def parseline(line):
    m = re.match(r"Card[ ]+([0-9]+): ([0-9 ]+) ; ([0-9 ]+)$", line)
    return (m.group(1), m.group(2), m.group(3))

def nb_winning_numbers(card):
    return len(list(set(card["win"]) & set(card["draw"])))

s = 0

with open("./4/input.txt") as f:
    for line in f.readlines():
        parsed = parseline(line.strip().replace("|", ";"))
        card = {"name": int(parsed[0]),
                    "win": [int(x) for x in parsed[1].strip().split(" ") if x],
                                "draw": [int(x) for x in parsed[2].strip().split(" ") if x]}
        cards.append(card)
        print(f"card {card['name']} has {nb_winning_numbers(card)} winning numbers: {pow(2, nb_winning_numbers(card) - 1)} points")
        if nb_winning_numbers(card) > 0:
            s += pow(2, nb_winning_numbers(card) - 1)
        
print(s)