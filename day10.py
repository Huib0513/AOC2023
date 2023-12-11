#!python3
import os
import datetime

# Test input
input = [
"-L|F7",
"7S-7|",
"L|7||",
"-L-J|",
"L|-JF"
]

#input = [
#"7-F7-",
#".FJ|7",
#"SJLL7",
#"|F--J",
#"LJ.LJ",
#]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def match_cell(direction, cell):
    match = False
    newdirection = direction

    index_newdir = orientation[cell].find(opposite_direction[direction])
    if (index_newdir != -1):
        match = True
        newdirection = orientation[cell][0 if index_newdir == 1 else 1]

    return match, newdirection


def solve1():
    row, col, result = 0,0,0
    while input[row][col] != 'S':
        col += 1
        if col == len(input[row]):
            col = 0
            row += 1
    print('Start is at (' + str(row) + ', ' + str(row) + ')')

    pipeline = [(row, col)]

    direction = 'E'
    newrow, newcol = row, col
    while (True):
        if (direction == 'E'):
            newrow = row
            newcol += 1
        if (direction == 'S'):
            newrow += 1
            newcol = col
        if (direction == 'W'):
            newrow = row
            newcol -= 1
        if (direction == 'N'):
            newrow -= 1
            newcol = col
        if (input[newrow][newcol] == 'S'): 
            break
        match, newdir = match_cell(direction, input[newrow][newcol])
        if (match):
            row = newrow
            col = newcol
            pipeline.append((row,col))
            direction = newdir
                
    #print(pipeline)

    print("Deel 1: " + str(len(pipeline)/2))

def solve2():
    print("Deel 2: No")

orientation = {'|': 'NS', '-': 'EW', 'L' : 'NE', 'J': 'NW', '7': 'SW', 'F': 'SE', '.': ''}
opposite_direction = {'N': 'S', 'E':'W', 'S':'N','W':'E'}

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
