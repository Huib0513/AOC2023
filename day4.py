#!python3
import os
import datetime
import re

# Test input
input = [
"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()


def solve1():
    mynums = {}
    winnums = {}
    t = {}
    for x,l in enumerate([l.split('|')[0].split(':')[1].split() for l in input]):
        mynums[x] = set([int(n) for n in l])
    for x,l in enumerate([l.split('|')[1].split() for l in input]):
        t[x] = mynums[x].intersection(set([int(n) for n in l]))
#        winnums[x] = set([int(n) for n in l])
#    for x in mynums.keys():
#        t[x] = mynums[x].intersection(winnums[x])

    result =0 
    for x in t:
        if (len(t[x]) > 0):
            result += 2**(len(t[x])-1)

    print("Deel 1: " + str(result))

def solve2():
    print("Deel 2: No")

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
