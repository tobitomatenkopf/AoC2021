if __name__ == '__main__':
    with open('day12challengefile.txt') as f:
        l = f.readlines()
def reverse(s):
    s.reverse()
    return s
puzzle = list(map(lambda s: s.strip('\n').split('-'), l))+list(map(lambda s: reverse(s.strip('\n').split('-')), l))

def pathFinding(location, counter = 0, visited = ['start']):
    if location == 'end':
        counter += 1
        return counter
    for con in puzzle:
        if con[0] == location and con[1] not in visited:
            if con[1].islower():
                visited.append(con[1])
            counter = pathFinding(con[1], counter, visited)
            if con[1].islower():
                visited.pop()
    return counter

def solve1():
    print(pathFinding('start'))

solve1()

def pathFinding2(location, counter = 0, visited = ['start'], visit2 = False):
    if location == 'end':
        counter += 1
        return counter
    for con in puzzle:
        if con[0] == location and con[1] not in visited and visit2 == True:
            if con[1].islower():
                visited.append(con[1])
            counter = pathFinding2(con[1], counter, visited, visit2)
            if con[1].islower():
                visited.pop()
        elif con[0] == location and visit2 == False and con[1] != 'start':
            if con[1] in visited:
                visit2 = True
            if con[1].islower():
                visited.append(con[1])
            counter = pathFinding2(con[1], counter, visited, visit2)
            visit2 = False
            if con[1].islower():
                visited.pop()

    return counter

def solve2():
    print(pathFinding2('start'))

solve2()
