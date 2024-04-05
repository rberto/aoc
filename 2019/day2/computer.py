prog = []

opcodes = [1,2,99]

def exec(index):
    op = prog[index]
    if not op in opcodes:
        return -2
    if op == 99:
        return -1

    arg1 = prog[prog[index+1]]
    arg2 = prog[prog[index+2]]
    result_index = prog[index+3]
    
    if op == 1:
        prog[result_index] = arg1 + arg2
        return index + 4
    elif op == 2:
        prog[result_index] = arg1 * arg2
        return index + 4

with open("./input", "r") as f:
    prog_org = [int(x) for x in f.readline().split(",")]

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
                break
        if prog[0] == 19690720:
            print(noun, verb)
            print(100*noun + verb)
