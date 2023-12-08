#!python3
import os
import datetime

# Test input
#input = ["RL",
#"",
#"AAA = (BBB, CCC)",
#"BBB = (DDD, EEE)",
#"CCC = (ZZZ, GGG)",
#"DDD = (DDD, DDD)",
#"EEE = (EEE, EEE)",
#"GGG = (GGG, GGG)",
#"ZZZ = (ZZZ, ZZZ)"]

#input = ["LLR",
#"",
#"AAA = (BBB, BBB)",
#"BBB = (AAA, ZZZ)",
#"ZZZ = (ZZZ, ZZZ)"]

input = ["LR",
"",
"11A = (11B, XXX)",
"11B = (XXX, 11Z)",
"11Z = (11B, XXX)",
"22A = (22B, XXX)",
"22B = (22C, 22C)",
"22C = (22Z, 22Z)",
"22Z = (22B, 22B)",
"XXX = (XXX, XXX)"]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()


def solve1():
    i, steps = 0, 0
    now = "AAA"
    while not now == "ZZZ":
        now = nodes[now][0 if route[i] == 'L' else 1]
        i += 1
        steps += 1
        if (i == len(route)): i = 0
    
    print("Deel 1: " + str(steps))

def solve2():
    i, steps = 0,0
    nows = {n for n in nodes.keys() if n[-1] == 'A'}
    while not (len(nows) == len([n for n in nows if n[-1] == 'Z'])):
        newnows = {nodes[n][0 if route[i] == 'L' else 1] for n in nows}
        nows = newnows
        i += 1
        steps += 1
        if (i == len(route)): i = 0
    print("Deel 2: " + str(steps))

route = input[0]
nodes = {x:(y.split(', ')[0][1:], y.split(', ')[1][:-1]) for x,y in [l.split(' = ') for l in input[2:]]}

start = datetime.datetime.now()
#solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
