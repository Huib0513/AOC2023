#!python3
import os
import datetime
from collections import defaultdict

# Test input
input = ["HASH"]
input = ["rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def gethash(input):
    result = 0
    for i in input:
        result += ord(i)
        result *= 17
        result = result % 256
    return result

def solve1():
    result = 0
    for i in input[0].split(','):
        result += gethash(i)

    print("Deel 1: " + str(result))

def solve2():
    result = 0
    boxes = {x:[] for x in range(256)}

    for step in input[0].split(','):
        if ((index := (step.find('='))) != -1):
            lens = step[:index]
            op = '='
            length = int(step[index+1:])
        else:
            lens = step[:-1]
            op = '-'
            length = 0
        box = gethash(lens)

        if (op == '-'):
            if len(boxes[box]) != 0:
                for k in boxes[box]:
                    if lens in k.keys(): 
                        boxes[box].remove(k)
        else:
            if (len(boxes[box]) == 0):
                boxes[box].append({lens: length})
            elif (lens in boxes[box][0].keys()):
                boxes[box][0][lens] = length
            else:
                boxes[box].append({lens: length})
    
    for n, box in [(b,boxes[b]) for b in boxes if len(boxes[b]) != 0]:
        print(n, [(n+1,b, list(b.values())[0]) for n,b in enumerate(box)])
        for o,b in enumerate(box):
            print(n+1, o+1, list(b.values())[0])
            result += (n+1) * (o+1) * list(b.values())[0]


    print("Deel 2: " + str(result))

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
