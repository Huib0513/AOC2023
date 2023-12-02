#!python3
import os
import datetime
import re

# Test input
input = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()


def solve1():
    result = 0
    maxcolors = {"red": 12, "green":13, "blue":14}

    for game in range(len(takes)):
        valid_game = True
        for t in takes[game]:
            for color in t:
                for key in maxcolors.keys():
                    if ((key in color) and (color[key] > maxcolors[key])):
                        valid_game = False
        if (valid_game):
            result += game + 1
    print("Deel 1: " + str(result))

def solve2():
    result = 0
    for game in takes:
        minreqcolors = {"blue": 0, "green": 0, "red":0}
        for t in game:
            for c in t:
                for color in c.keys():
                    if (c[color] > minreqcolors[color]):
                        minreqcolors[color] = c[color]
        #print(game, minreqcolors)
        power = 1
        for mr in minreqcolors.values():
            power = power * mr
        result += power

    print("Deel 2: " + str(result))

takes = [[[{cl.split(' ')[1]:int(cl.split(' ')[0])} for cl in color.split(', ')] for color in y.split('; ')] for x,y in [l.split(': ') for l in input]]

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
