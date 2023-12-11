#!python3
import os
import datetime

# Test input
input = [
"0 3 6 9 12 15",
"1 3 6 10 15 21",
"10 13 16 21 30 45"
]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def get_end(list):
    if (len(list) == len([x for x in list if x==0])):
        return 0
    lowerlist = [list[x+1]-list[x] for x in range(len(list)-1)]
    #print(list, lowerlist)
    return get_end(lowerlist) + list[-1]

def solve1():
    result = 0
    values = []
    for l in input:
        values.append([int(x) for x in l.split()])
    print(values)

    result = 0
    for x in values:
        result += get_end(x)

    print("Deel 1: " + str(result))

    result = 0
    for x in values:
        result += get_end(list(reversed(x)))

    print('Deel 2: ' + str(result))

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)
