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
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

maporder = ["seed-to-soil","soil-to-fertilizer","fertilizer-to-water","water-to-light","light-to-temperature","temperature-to-humidity","humidity-to-location"]

# def get_maps_old(input, maps):
#     for line in input[2:]:
#         if len(line) == 0: continue
#         if line.find('map') > 0:
#             currentmap = line.split()[0]
#             print('Processing map ' + currentmap)
#             maps[currentmap] = {}
#             continue
#         dest, source, length = [int(x) for x in line.split()]
#         maps[currentmap].update(dict(zip(range(source, source+length), range(dest, dest+length))))

def get_maps(input, maps):
    for line in input[2:]:
        if len(line) == 0: continue
        if line.find('map') > 0:
            currentmap = line.split()[0]
            print('Processing map ' + currentmap)
            maps[currentmap] = {}
            rangecount = 0
            continue
        dest, source, length = [int(x) for x in line.split()]
        maps[currentmap].update({rangecount:(source, source+length-1, dest)})
        rangecount += 1

def transition(source, map):
    #         if location[s] in maps[maporder[i]]:
    #             location[s] = maps[maporder[i]][location[s]]
    #         else:
    #             location[s] = location[s]

    return source

def solve1():
    solutions = {int(x):int(x) for x in input[0].split(': ')[1].split()}
    for i in range(len(maporder)):
        #print(solutions)
        for s in solutions:
            for r in (maps[maporder[i]].values()):
                if ((solutions[s] >= r[0]) and (solutions[s] <= r[1])):
                    solutions[s] = r[2] + (solutions[s] - r[0])
                    break
    print("Deel 1: " + str(min(solutions.values())))

    # Lazy option: copy code for part 2
    # solutions = {}
    # seeds = [int(x) for x in input[0].split(': ')[1].split()]
    # for x in range(0, len(seeds),2):
    #     for t in range(seeds[x+1]):
    #         solutions[seeds[x]+t]=seeds[x]+t
    # for i in range(len(maporder)):
    #     #print(solutions)
    #     for s in solutions:
    #         for r in (maps[maporder[i]].values()):
    #             if ((solutions[s] >= r[0]) and (solutions[s] <= r[1])):
    #                 solutions[s] = r[2] + (solutions[s] - r[0])
    #                 break
    #print("Deel 2: " + str(min(solutions.values())))

# def old_solve1():
#     print(maps)
#     location = {int(x):int(x) for x in input[0].split(': ')[1].split()}
#     print(location)
#     for i in range(len(maporder)):
#         for s in location:
#             if location[s] in maps[maporder[i]]:
#                 location[s] = maps[maporder[i]][location[s]]
#             else:
#                 location[s] = location[s]
#         print('After ' + maporder[i] + ": ")
#         print(location)

#     #print((location.values()))
#     print("Deel 1: " + str(min(location.values())))

def solve2():
    seeds = [int(x) for x in input[0].split(': ')[1].split()]
    location = [(int(seeds[x]),int(seeds[x])+int(seeds[x+1]-1)) for x in range(0,len(seeds),2)]
    print(location)
    for i in range(len(maporder)):
        newlocations = []
        for s in location:
            newlocations.append(transition(s, maps[maporder[i]]))
        location = newlocations
        print('After ' + maporder[i] + ": ")
        print(location)
    print("Deel 2: No")


seeds = [int(x) for x in input[0].split(': ')[1].split()]
maps = {}
get_maps(input, maps)

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
