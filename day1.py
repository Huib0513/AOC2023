#!python3
import os
import datetime
import re

# Test input
#input = ["1abc2",
#"pqr3stu8vwx",
#"a1b2c3d4e5f",
#"treb7uchet"]

input = ["two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen"]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

numbers = {"1": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0, 
 "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

def solve1():
    #print({x for x in [l for l in input]})
    result = 0
    for l in input:
        ld = []
        for x in l:
            if (x.isdigit()):
                ld.append(int(x))
        result += ld[0]*10 + ld[-1]
    print("Deel 1: " + str(result))

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def solve2():
    result = 0
    for l in input:
        min = ""
        minpos = len(l)
        max = ""
        maxpos = -1
        for n in numbers.keys():
            for np in find_all(l, n):
                print(n, np)
                if (np > maxpos):
                    max = n
                    maxpos = np
                if (np < minpos):
                    min = n
                    minpos = np
        print(numbers[min]*10 + numbers[max])
        result += numbers[min]*10 + numbers[max]
    
    print("Deel 2: " + str(result))

start = datetime.datetime.now()
#solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
