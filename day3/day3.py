def readFile():
    with open('day3challengefile.txt', 'r') as f:
        return list(map(lambda s: s.strip('\n'), f.readlines()))

if __name__ == '__main__':
    l = readFile()
    #part1
    gamma = ''
    for digit in range(len(l[0])):
        oneCounter = 0
        zeroCounter = 0
        for binary in l:
            if binary[digit] == '0':
                zeroCounter += 1
            else:
                oneCounter += 1
        if oneCounter > zeroCounter:
            gamma += '1'
        else:
            gamma += '0'
    gamma = int(gamma, 2)
    epsilon = ''
    for digit in range(len(l[0])):
        oneCounter = 0
        zeroCounter = 0
        for binary in l:
            if binary[digit] == '0':
                zeroCounter += 1
            else:
                oneCounter += 1
        if oneCounter > zeroCounter:
            epsilon += '0'
        else:
            epsilon += '1'
    epsilon = int(epsilon, 2)

    print(epsilon*gamma)

    #part2
    oxy = None
    solutionList = l
    for digit in range(len(l[0])):
        if len(solutionList) == 1:
            break
        oneCounter = 0
        zeroCounter = 0
        for binary in solutionList:
            if binary[digit] == '0':
                zeroCounter += 1
            else:
                oneCounter += 1
        if oneCounter > zeroCounter:
            newSolList = []
            for s in solutionList:
                if s[digit] == '1':
                    newSolList.append(s)
            solutionList = newSolList
        elif oneCounter == zeroCounter:
            newSolList = []
            for s in solutionList:
                if s[digit] == '1':
                    newSolList.append(s)
            solutionList = newSolList
        else:
            newSolList = []
            for s in solutionList:
                if s[digit] == '0':
                    newSolList.append(s)
            solutionList = newSolList
    oxy = int(solutionList[0], 2)

    o2 = None
    solutionList = l
    for digit in range(len(l[0])):
        if len(solutionList) == 1:
            break
        oneCounter = 0
        zeroCounter = 0
        for binary in solutionList:
            if binary[digit] == '0':
                zeroCounter += 1
            else:
                oneCounter += 1
        if oneCounter > zeroCounter:
            newSolList = []
            for s in solutionList:
                if s[digit] == '0':
                    newSolList.append(s)
            solutionList = newSolList
        elif oneCounter == zeroCounter:
            newSolList = []
            for s in solutionList:
                if s[digit] == '0':
                    newSolList.append(s)
            solutionList = newSolList
        else:
            newSolList = []
            for s in solutionList:
                if s[digit] == '1':
                    newSolList.append(s)
            solutionList = newSolList
    o2 = int(solutionList[0], 2)
    print(oxy*o2)
