if __name__ == '__main__':
    with open('day11challengefile.txt') as f:
        l = f.readlines()

l = list(map(lambda s: s.strip('\n'), l))
input = []
for row in l:
    rowNumbs = []
    for numb in row:
        rowNumbs.append(int(numb))
    input.append(rowNumbs)

def getNeighbours(x, y, width, height):
    neighbours = []
    for changeX in [-1, 0, 1]:
        for changeY in [-1, 0, 1]:
            if width > x+changeX >= 0 and height > y+changeY >= 0 and (x-changeX, y-changeY) != (x, y):
                neighbours.append((x+changeX, y+changeY))
    return neighbours

def solve1():
    flashes = 0
    for i in range(100):
        for x, row in enumerate(input): # [a, b, c] -> [(0, a), (1, b), (2, c)]
            for y, energy in enumerate(row):
                input[x][y] += 1

        alreadyFlashed = []
        greater9 = True
        while greater9:
            greater9 = False
            for x, row in enumerate(input):
                for y, energy in enumerate(row):
                    if energy > 9 and (x, y) not in alreadyFlashed:
                        alreadyFlashed.append((x, y))
                        flashes += 1
                        for neighbourX, neighbourY in getNeighbours(x, y, len(input), len(row)):
                            input[neighbourX][neighbourY] += 1
                            greater9 = True

        for x, row in enumerate(input): # [a, b, c] -> [(0, a), (1, b), (2, c)]
            for y, energy in enumerate(row):
                if energy > 9:
                    input[x][y] = 0
    return flashes
print(solve1())


if __name__ == '__main__':
    with open('day11challengefile.txt') as f:
        l = f.readlines()

l = list(map(lambda s: s.strip('\n'), l))
input = []
for row in l:
    rowNumbs = []
    for numb in row:
        rowNumbs.append(int(numb))
    input.append(rowNumbs)

def solve2():
    i = 1
    while True:
        for x, row in enumerate(input): # [a, b, c] -> [(0, a), (1, b), (2, c)]
            for y, energy in enumerate(row):
                input[x][y] += 1

        alreadyFlashed = []
        greater9 = True
        while greater9:
            greater9 = False
            for x, row in enumerate(input):
                for y, energy in enumerate(row):
                    if energy > 9 and (x, y) not in alreadyFlashed:
                        alreadyFlashed.append((x, y))
                        for neighbourX, neighbourY in getNeighbours(x, y, len(input), len(row)):
                            input[neighbourX][neighbourY] += 1
                            greater9 = True

        for x, row in enumerate(input): # [a, b, c] -> [(0, a), (1, b), (2, c)]
            for y, energy in enumerate(row):
                if energy > 9:
                    input[x][y] = 0

        if all(all(energy == 0 for energy in row) for row in input):
            return i
        i += 1
print(solve2())
