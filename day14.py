#!python3
import os
import datetime

# Test input
input = [
"O....#....",
"O.OO#....#",
".....##...",
"OO.#O....O",
".O.....O#.",
"O.#..O.#.#",
"..O..#O..O",
".......O..",
"#....###..",
"#OO..#...."
]

# input complete lines
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()


def solve1():
    result = 0
    shifted_rocks = {c:rocks[c] for c in rocks if rocks[c] =='#' }

    for r in rocks:
        if rocks[r] == '#': continue
        for above in reversed(range(r[0])):
            if ((above,r[1]) in shifted_rocks):
                shifted_rocks[above+1,r[1]] = rocks[r]
                print('Move ' + str(r) + ' to ' + str((above, r[1])))
                break

    print(sorted(shifted_rocks))
    print("Deel 1: " + str(result))

def solve2():
    print("Deel 2: No")

rocks = {}
for row in range(len(input)):
    rocks = rocks | {(row, col):type for (col,type) in [(c,input[row][c]) for c in range(len(input[row])) if input[row][c] != '.']}
print(rocks)

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
