#!python3
import os
import datetime
import re

# Test input
input = [
"seeds: 79 14 55 13",
"",
"seed-to-soil map:",
"50 98 2",
"52 50 48",
"",
"soil-to-fertilizer map:",
"0 15 37",
"37 52 2",
"39 0 15",
"",
"fertilizer-to-water map:",
"49 53 8",
"0 11 42",
"42 0 7",
"57 7 4",
"",
"water-to-light map:",
"88 18 7",
"18 25 70",
"",
"light-to-temperature map:",
"45 77 23",
"81 45 19",
"68 64 13",
"",
"temperature-to-humidity map:",
"0 69 1",
"1 0 69",
"",
"humidity-to-location map:",
"60 56 37",
"56 93 4"
]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

# Parse input
maporder = ["seed-to-soil","soil-to-fertilizer","fertilizer-to-water","water-to-light","light-to-temperature","temperature-to-humidity","humidity-to-location"]

seeds = [int(x) for x in input[0].split(': ')[1].split()]

maps = {}
for line in input[2:]:
    if len(line) == 0: continue
    if line.find('map') > 0:
        currentmap = line.split()[0]
        print('Processing map ' + currentmap)
        maps[currentmap] = {}
        continue
    dest, source, length = [int(x) for x in line.split()]
    maps[currentmap].update(dict(zip(range(source, source+length), range(dest, dest+length))))
    



def solve1():
    print(maps)
    location = {int(x):int(x) for x in input[0].split(': ')[1].split()}
    print(location)
    for i in range(len(maporder)):
        for s in location:
            if location[s] in maps[maporder[i]]:
                location[s] = maps[maporder[i]][location[s]]
            else:
                location[s] = location[s]
        print('After ' + maporder[i] + ": ")
        print(location)

    #print((location.values()))
    print("Deel 1: " + str(min(location.values())))

def solve2():
    print("Deel 2: No")

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
