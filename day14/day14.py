from collections import defaultdict
from timeit import timeit

with open('day14challengefile.txt') as f:
    l = f.readlines()

start = l[0].strip('\n')
instructionsList = list(map(lambda s: s.strip('\n').split(' -> '), l[2:]))
instructions = defaultdict()
for instr in instructionsList:
    instructions[instr[0]] = instr[1]

def solve1(start):
    for i in range(10):
        previous = start[0]
        newStart = ''
        for char in start[1:]:
            newStart += previous
            for instr in instructionsList:
                if instr[0] == previous+char:
                    newStart += instr[1]
                    break
            previous = char
        newStart += start[-1]
        start = newStart
    count1 = []
    count2 = []

    for char in start:
        if char in count1:
            count2[count1.index(char)] += 1
        else:
            count1.append(char)
            count2.append(1)
    solution = max(count2) - min(count2)
    print(solution)

solve1(start)

def solve2():
    lastLetter = start[-1]
    keyAmountBefore = defaultdict(int)
    for elem in zip(start, start[1:]):
        keyAmountBefore[''.join(elem)] += 1


    for i in range(40):
        keyAmountAfter = defaultdict(int)
        for key, amount in keyAmountBefore.items():
            key1 = key[0] + instructions[key]
            key2 = instructions[key] + key[1]
            keyAmountAfter[key1] += amount
            keyAmountAfter[key2] += amount
        keyAmountBefore = keyAmountAfter.copy()


    solutionDic = defaultdict(int)
    for key, amount in keyAmountBefore.items():
        solutionDic[key[0]] += amount
    solutionDic[lastLetter] += 1
    solution = solutionDic[max(solutionDic, key = solutionDic.get)] - solutionDic[min(solutionDic, key = solutionDic.get)]
    print(solution)

solve2()
