def readFile():
    with open('day2challengefile.txt', 'r') as f:
        l = f.readlines()
        l = list(map(lambda s: s.strip('\n'), l))
        return l

if __name__ == '__main__':
    l = readFile()
    horizontal = 0
    depth = 0
    for e in l:
        newe = e.split(' ')
        if newe[0] == 'forward':
            horizontal += int(newe[1])
        elif newe[0] == 'down':
            depth += int(newe[1])
        else:
            depth -= int(newe[1])
    print(depth*horizontal)

    horizontal = 0
    depth = 0
    aim = 0
    for e in l:
        newe = e.split(' ')
        if newe[0] == 'forward':
            horizontal += int(newe[1])
            depth += aim*int(newe[1])
        elif newe[0] == 'down':
            aim += int(newe[1])
        else:
            aim -= int(newe[1])
    print(depth*horizontal)
