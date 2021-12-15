def readFile():
    with open('day1challengefile1.txt', 'r') as f:
        l = f.readlines()
        l = list(map(lambda s: s.strip('\n'), l))
        return list(map(lambda s : int(s), l))

if __name__ == '__main__':
    l = readFile()
    counter = -1
    previousNumb = -1
    for numb in l:
        if numb > previousNumb:
            counter += 1
        previousNumb = numb
    print('task1:' + str(counter))

    newl = []
    n = 0
    for numb in l:
        if n+3 > len(l):
            break
        else:
            newl.append(numb + l[n+1] + l[n+2])
        n += 1
    counter = -1
    previousNumb = -1
    for numb in newl:
        if numb > previousNumb:
            counter += 1
        previousNumb = numb
    print('task2:' + str(counter))
