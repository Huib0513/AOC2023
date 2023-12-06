#!python3
import os
import datetime
import re

# Test input
input = ["Time:      7  15   30",
"Distance:  9  40  200"]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()


def solve1():
    distance = {}
    duration = [int(x) for x in input[0].split(':')[1].split()]
    maxjes = [int(x) for x in input[1].split(':')[1].split()]
    for i,d in enumerate(duration):
        distance[d] = [x*(d-x) for x in range(d+1) if (x*(d-x) > maxjes[i])]
    #print(duration, distance)
    result = 1
    for d in distance:
        result *= len(distance[d])
    print("Deel 1: " + str(result))

def solve2():
    duration = int("".join(input[0].split(':')[1].split()))
    maxje = int("".join(input[1].split(':')[1].split()))
    print(duration, maxje)
    distance = [x*(duration-x) for x in range(duration) if (x*(duration-x) > maxje)]
    print("Deel 2: " + str(len(distance)))

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
