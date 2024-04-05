import subprocess
from subprocess import PIPE
import itertools
import time

def launchamp(phase):
    a = subprocess.Popen(["python3", "computer.py"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    p = str(phase) + "\n"
    a.stdin.write(p.encode())
    a.stdin.flush()
    return a

def sendsignal(signal, amp):
    m = str(signal) + "\n"
    amp.stdin.write(m.encode())
    amp.stdin.flush()
    time.sleep(0.1)
    return int(amp.stdout.readline().decode().strip())
    
def runmultipleamps(p):
    amps = []
    inpu = 0
    i = 0
    for phase in p:
        amps.append(launchamp(phase))

    while amps[-1].poll() == None:
        inpu = sendsignal(inpu, amps[i])
        #print(inpu)
        i += 1
        if i >= len(amps):
            i = 0
    return inpu

results = []

for p in list(itertools.permutations([5, 6, 7, 8, 9])):
    print(p)
    r = runmultipleamps(p)
    results.append(r)
    print(results)

print(results)
print("MAX:", max(results))
