"""
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""

digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five":5, "six":6, "seven": 7, "eight":8, "nine":9}

def findalloccurence(string, sub):
    import re
    return [m.start() for m in re.finditer(sub, string)]

def findalldigits(string):
    alldigits = {}
    for i in digits.values():
        for index in findalloccurence(string, str(i)):
            alldigits[index] = i

    for digit in digits.keys():
        for index in findalloccurence(string, digit):
            alldigits[index] = digits[digit]
    return alldigits

def findfirstdigit(alldigits):
    return(alldigits[min(alldigits.keys())])

def findlastdigit(alldigits):
    return(alldigits[max(alldigits.keys())])

sum = 0

with open("/home/romain/Documents/code/aoc2023/1/input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        alldigits = findalldigits(line)
        first = findfirstdigit(alldigits)
        second = findlastdigit(alldigits)
        sum = sum + int(f"{first}{second}")

print(sum)
