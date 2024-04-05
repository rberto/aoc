from enum import Enum
import sys

prog = []

opcodes = {}

def add(args, op):
    #print(args[0], "+", args[1])
    return args[0]+args[1], index + op["nbargs"]+1

def mult(args, op):
    #print(args[0], "*", args[1])
    return args[0]*args[1], index + op["nbargs"]+1

def read(args, op):
    return input("Input:"), index + op["nbargs"]+1

def output(args, op):
    print(args[0])
    return None, index + op["nbargs"]+1

def end(args, op):
    quit()

def jumpiftrue(args, op):
    if args[0] != 0:
        return None, args[1]
    else:
        return None, index + op["nbargs"]+1

def jumpiffalse(args, op):
    if args[0] == 0:
        return None, args[1]
    else:
        return None, index + op["nbargs"]+1

def lessthan(args, op):
    if args[0] < args[1]:
        return 1, index + op["nbargs"]+1
    else:
        return 0, index + op["nbargs"]+1

def equal(args, op):
    if args[0] == args[1]:
        return 1, index + op["nbargs"]+1
    else:
        return 0, index + op["nbargs"]+1

    
addition = {"id": 1, "nbargs": 3, "func": add}
multiply = {"id": 2, "nbargs": 3, "func": mult}
read = {"id": 3, "nbargs": 1, "func": read}
output = {"id": 4, "nbargs": 1, "func": output}
fin = {"id": 99, "nbargs": 0, "func": end}

jit = {"id": 5, "nbargs": 2, "func": jumpiftrue}
jif = {"id": 6, "nbargs": 2, "func": jumpiffalse}
lt = {"id": 7, "nbargs": 3, "func": lessthan}
eq = {"id": 8, "nbargs": 3, "func": equal}

#opcodes = [i for i in range(0,100)]

opcodes[1] = addition
opcodes[2] = multiply
opcodes[3] = read
opcodes[4] = output
opcodes[5] = jit
opcodes[6] = jif
opcodes[7] = lt
opcodes[8] = eq
opcodes[99] = fin

#print(opcodes)

#opcodes[99] = fin

class mode(Enum):
    POSITION = 0
    IMMEDIATE = 1

def instructionparse(instr):
    #print("instr", instr)
    opcode = (instr%100)
    #print("opcode", opcode)
    param1mode = mode(int((instr / 100)%10))
    #print("param1mode=", param1mode)
    param2mode = mode(int((instr / 1000)%10))
    param3mode = mode(int((instr / 10000)%10))
    return (opcode, [param1mode, param2mode, param3mode])
    
def exec(index):
    op, modes = instructionparse(prog[index])
    print(op, modes)
    
    args = [0 for i in range(0, opcodes[op]["nbargs"])]
    values = [0 for i in range(0, opcodes[op]["nbargs"])]
    
    for i in range(0, opcodes[op]["nbargs"]):
        args[i] = prog[index+i+1]
        if modes[i] == mode.POSITION:
            #print("prog[args[i]]=", prog[args[i]])
            values[i] = int(prog[args[i]])
            #print(values[i])
        else:
            values[i] = int(args[i])
    print("values", values)
    #print("args", args)
    
    result, newindex = opcodes[op]["func"](values, opcodes[op])
    if result != None:
        prog[args[-1]] = result

    return newindex


with open("./input", "r") as f:
    prog = [int(x) for x in f.readline().split(",")]

#print(prog)
#prog = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
index = 0
while index != -1:
    index = exec(index)
    #print("current", index)
    if index == -2:
        print("Error")
        break




"""
for noun in range(0,99):
    for verb in range(0,99):
        prog = list(prog_org)
        prog[1]=noun
        prog[2]=verb
        index = 0
        while index != -1:
            index = exec(index)
            #print(prog)
            if index == -2:
#                print("Error")
break$
        if prog[0] == 19690720:
            print(noun, verb)
            print(100*noun + verb)
"""
