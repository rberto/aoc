import math

def get_infos(instruction):
    a = instruction[0]
    d = int(instruction[1:].strip())
    return (a, d)

def move(current, a):
    if a == "U":
        return (current[0], current[1]+1)
    elif a == "D":
        return (current[0], current[1]-1)
    elif a == "R":
        return (current[0]+1, current[1])
    elif a == "L":
        return (current[0]-1, current[1])

def getvisited(wire):
    visited = []
    current = (0,0)
    for instruction in wire:
        (a, d) = get_infos(instruction)
        for i in range(0, d):
            current = move(current, a)
            visited.append(current)
    return visited

def inters_path_l(v1, v2):
    inters = []
    for p in v1:
        if p in v2:
            #print(p)
            #print(v1, v2)
            i1 = v1.index(p) + 1
            i2 = v2.index(p) + 1
            #print(str(i1) + " dfdf "+ str(i2))
            inters.append(i1 + i2)
    return inters

def dist(p):
    return abs(p[0])+abs(p[1])


with open("./input", "r") as f:
    wire1 = f.readline().split(",")
    #print(wire1)
    wire2 = f.readline().split(",")
    #print(wire2)   
    #wire1 = ["R8","U5","L5","D3"]#["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
    #wire2 = ["U7","R6","D4","L4"]#["U62","R66","U55","R34","D71","R55","D58","R83"]
    visited1 = getvisited(wire1)
    visited2 = getvisited(wire2)
    #print(visited2)
    #print(visited1)
    i = inters_path_l(visited2, visited1)
    #print(i)
    #ds = [dist(p) for p in i]
    print(min(i))
    
        
