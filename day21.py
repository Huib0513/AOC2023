#!python3
import os
import datetime

# Test input
input = [
"...........",
".....###.#.",
".###.##..#.",
"..#.#...#..",
"....#.#....",
".##..S####.",
".##..#...#.",
".......##..",
".##.#.####.",
".##..##.##.",
"..........."
]

# input complete lines
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def get_plots_in_one_step(startposition):
    result = []

    for row in range(max(0, startposition[0]-1), min(startposition[0]+1, len(input))):
        for col in range(max(0, startposition[1]-1), min(startposition[1]+1, len(input[0]))):
            if (row,col) in plots:
                result.append((row,col))

    return result

def solve1():
    result = 0
    reachable_plots = []

    reachable_plots.append(get_plots_in_one_step(elfstart))

    print(reachable_plots)

    print("Deel 1: " + str(result))

def solve2():
    print("Deel 2: No")

plots = []
for r,l in enumerate(input):
    for c in range(len(l)):
        if l[c] == '.':
            plots.append((r,c))
        elif l[c] == 'S':
            elfstart = (r,c)
    #plots.append([(r,c) for c in range(len(l)) if l[c] == '.'])
    #if l[c] == 'S': start = (r,c)
print(plots)
print(elfstart)


start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
