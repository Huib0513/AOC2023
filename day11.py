#!python3
import os
import datetime

# Test input
input = [
"...#......",
".......#..",
"#.........",
"..........",
"......#...",
".#........",
".........#",
"..........",
".......#..",
"#...#....."
]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def get_lengths(coordinates):
    result = 0
    if (len(coordinates) == 1):
        result = 0
    else:
        result = get_lengths(coordinates[1:])
        curlengths = [abs(coordinates[0][0]-c[0]) + abs(coordinates[0][1] - c[1]) for c in coordinates[1:]]
        result += sum(curlengths) #sum([(abs(coordinates[0][0])-abs(c[0])) + (abs(coordinates[1]) - abs(c[1])) for c in coordinates[1:]])
    return result

def solve1(expansion):
    result, expanded_row = 0, 0
    galaxies, empty_columns = [], []

    for col in range(len(input[0])):
        if (len([input[row][col] for row in [x for x in range(len(input))] if input[row][col] == '#']) == 0):
            empty_columns.append(col)
    #print(empty_columns)

    for r in range(len(input)):
        if (input[r].find('#') == -1):
            expanded_row += expansion
        else:
            for g in [(expanded_row,col) for col in [c for c in range(len(input[r])) if input[r][c] == '#'] ]:
                galaxies.append(g)
        expanded_row += 1
    #print(galaxies)

    # shift columns
    for c in sorted(empty_columns, reverse = True):
        newgalaxies = []
        for g in galaxies:
            if g[1] > c:
                newgalaxies.append((g[0], g[1]+expansion))
            else:
                newgalaxies.append(g)
        galaxies = newgalaxies
    #print(galaxies)

    print("Deel 1: " + str(get_lengths(galaxies)))

def solve2():
    print("Deel 2: No")

start = datetime.datetime.now()
solve1(1)
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve1(999999)
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
