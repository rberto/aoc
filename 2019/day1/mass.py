import math
modules = []
sum = 0

def get_fuel(mass):
    return math.floor(mass/3) - 2

def get_all_fuel(mass):
    result = 0
    new_mass = mass
    new_fuel = 1
    while new_fuel > 0:
        new_fuel = get_fuel(new_mass)
        if (new_fuel > 0):
            result += new_fuel
        print(result)
        new_mass = new_fuel
    return result

with open("./input", "r") as f:

    for line in f.readlines():
        mass = int(line)
        modules.append(mass)
        fuel = get_all_fuel(mass)
        sum += fuel

print(sum)

