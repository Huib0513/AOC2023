#!python3
import os
import datetime
from collections import Counter
from functools import cmp_to_key

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
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

cardorder = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
typeorder = {'fiveofakind': 7, 'fourofakind': 6, 'fullhouse': 5, 'threeofakind': 4, 'twopair': 3, 'onepair': 2, 'highcard': 1}

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

def handcompare(hand1, hand2):
    #powers = [2**cardorder.index(x) for x in hand]
    result = 0
    if typeorder[get_type(hand1)] < typeorder[get_type(hand2)]:
        result = -1
    elif typeorder[get_type(hand1)] > typeorder[get_type(hand2)]:
        result = 1
    else:
        for x in range(len(hand1)):
            if cardorder.index(hand1[x]) < cardorder.index(hand2[x]):
                result = -1
                break
            elif cardorder.index(hand1[x]) > cardorder.index(hand2[x]):
                result = 1
                break
    return result

def solve1():
    hands = {l.split()[0]:typeorder[get_type(l.split()[0])] for l in input}
    bets = {l.split()[0]:int(l.split()[1]) for l in input}
    #print(hands, bets)
    handlist = list(hands)

    #print(sorted(hands, key = cmp_to_key(handcompare)))

    value = sum([(x+1)*bets[y] for x,y in enumerate(sorted(hands, key = cmp_to_key(handcompare)))])

    print("Deel 1: " + str(value))

def solve2():
    print("Deel 2: No")

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
