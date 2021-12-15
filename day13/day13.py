with open('day13challengefile.txt') as f:
    l = f.readlines()
inpPaper = list(map(lambda s: s.strip('\n').split(','), l[:l.index('\n')]))
instructions = list(map(lambda s: [s[0], int(s[1])] ,list(map(lambda s: s.strip('\n').strip('fold along ').split('='), l[l.index('\n')+1:]))))

def printBoard(paper):
    for row in paper:
        print(''.join(row))

size = [0, 0]
for loc in inpPaper:
    size[1] = max(int(loc[1]), size[1])
    size[0] = max(int(loc[0]), size[0])

def solve1():
    paper = [['.' for i in range(size[0]+1)] for i in range(size[1]+1)]

    for loc in inpPaper:
        paper[int(loc[1])][int(loc[0])] = '#'

    instruction = instructions[0]
    if instruction[0] == 'x':
        for y, row in enumerate(paper):
            for x, sign in enumerate(row):
                if sign == '#' and x > instruction[1]:
                    paper[y][2*instruction[1] - x] = '#'
            paper[y] = paper[y][:instruction[1]]
    if instruction[0] == 'y':
        for y, row in enumerate(paper):
            for x, sign in enumerate(row):
                if sign == '#' and y > instruction[1]:
                    paper[2*instruction[1] - y][x] = '#'
        paper = paper[:instruction[1]]
    points = 0
    for row in paper:
        for sign in row:
            if sign == '#':
                points += 1
    print(points)

solve1()

def solve2():
    paper = [['.' for i in range(size[0]+1)] for i in range(size[1]+1)]

    for loc in inpPaper:
        paper[int(loc[1])][int(loc[0])] = '#'

    for instruction in instructions:
        if instruction[0] == 'x':
            for y, row in enumerate(paper):
                for x, sign in enumerate(row):
                    if sign == '#' and x > instruction[1]:
                        paper[y][2*instruction[1] - x] = '#'
                paper[y] = paper[y][:instruction[1]]
        if instruction[0] == 'y':
            for y, row in enumerate(paper):
                for x, sign in enumerate(row):
                    if sign == '#' and y > instruction[1]:
                        paper[2*instruction[1] - y][x] = '#'
            paper = paper[:instruction[1]]
    printBoard(paper)

solve2()
