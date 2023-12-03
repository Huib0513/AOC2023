#!python3
import os
import datetime
from collections import defaultdict

# Test input
input =[
"467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598.."]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def solve1():
    numbers = {}
    symbols = {}
    possible_gears = defaultdict(list)
    # Parse input
    for row in range(len(input)):
        #print(row)
        col = 0
        while (col < len(input[row])):
            if (input[row][col].isdigit()):
                startcol = col
                numbers[(row,startcol)] = input[row][col]
                col += 1
                while ((col < len(input[row])) and (input[row][col].isdigit())):
                    numbers[(row,startcol)] += input[row][col]
                    col += 1
                continue
            elif (input[row][col] != '.'):
                symbols[(row,col)] = input[row][col]
            col += 1
#    print(symbols)
    
    # Do work
    result1 = 0
    for num in numbers.keys():
        countit = False
        for cr in range(num[0]-1,num[0]+2):
            for cc in range(num[1]-1,num[1]+len(numbers[num])+1):
                if ((cr,cc) in symbols.keys()):
                    countit = True
                    if (symbols[cr,cc] == "*"):
                        possible_gears[(cr,cc)].append(num)
        if (countit): 
            result1 += int(numbers[num])

    print("Deel 1: " + str(result1))

    #print([x for x in possible_gears.keys() if len(possible_gears[x])==2])
    result2 = 0
    for g in [x for x in possible_gears.keys() if len(possible_gears[x])==2]:
        #print(possible_gears[g])
        #print(numbers[possible_gears[g][0]], numbers[possible_gears[g][1]])
        result2 += int(numbers[possible_gears[g][0]]) * int(numbers[possible_gears[g][1]])
    # Do check
    print("Deel 2: " + str(result2))

def solve2():
    print("Deel 2: No")

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
