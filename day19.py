#!python3
import os
import datetime

# Test input
input = [
"px{a<2006:qkq,m>2090:A,rfg}",
"pv{a>1716:R,A}",
"lnx{m>1548:A,A}",
"rfg{s<537:gd,x>2440:R,A}",
"qs{s>3448:A,lnx}",
"qkq{x<1416:A,crn}",
"crn{x>2662:A,R}",
"in{s<1351:px,qqz}",
"qqz{s>2770:qs,m<1801:hdj,R}",
"gd{a>3333:R,R}",
"hdj{m>838:A,pv}",
"",
"{x=787,m=2655,a=1222,s=2876}",
"{x=1679,m=44,a=2067,s=496}",
"{x=2036,m=264,a=79,s=2244}",
"{x=2461,m=1339,a=466,s=291}",
"{x=2127,m=1623,a=2188,s=1013}"
]

# input complete lines
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def flow_work(wfkey, item):
    result = 'R'
    for step in workflows[wfkey]:
        if ((index := step.find(':')) != -1):
            check = step[:index]
            nextstep = step[index+1:]
            print(check, nextstep)
        else:
            nextstep = step
            print(step)
        
    return(result)

def solve1():
    result = 0
    results = []
    for i in items:
        if flow_work('in', i) == 'A':
            results.append(i)

    print("Deel 1: " + str(result))

def solve2():
    print("Deel 2: No")

readitems = False
items, workflows = [], {}
for l in input:
    if len(l) == 0: 
        readitems = True
        continue
    if readitems:
        items.append({kv.split('=')[0]:kv.split('=')[1] for kv in l[1:len(l)-1].split(',')})
    else:
        workflows[l.split('{')[0]] = [s for s in l.split('{')[1][:len(l.split('{')[1])-1].split(',')]

print(workflows, items)

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
