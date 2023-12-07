#!python3
import os
import datetime
from collections import Counter

# Test input
input = ["32T3K 765",
"T55J5 684",
"KK677 28",
"KTJJT 220",
"QQQJA 483"]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

cardorder = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
typeorder = {'fiveofakind': 1, 'fourofakind': 2, 'fullhouse': 3, 'threeofakind': 4, 'twopair': 5, 'onepair': 6, 'highcard': 7}

def get_type(hand):
    c = Counter(hand)
    match max(c.values()):
        case 5:
            return 'fiveofakind'
        case 4: 
            return 'fourofakind'
        case 1: 
            return 'highcard'
        case 2: 
            if len(c) == 3: 
                return'twopair'
            else:
                return 'onepair'
        case 3: 
            if len(c) == 3:
                return 'threeofakind'
            else:
                return 'fullhouse'


def solve1():
    hands = {l.split()[0]:typeorder[get_type(l.split()[0])] for l in input}
    bets = [l.split()[1] for l in input]
    print(hands)

    print("Deel 1: No")

def solve2():
    print("Deel 2: No")

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
