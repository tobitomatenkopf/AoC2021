if __name__ == '__main__':
    with open('day5challengefile.txt', 'r') as f:
        l = f.readlines()

    #part1
    positions = []
    doublePositions = []
    for line in l:
        ends = list(map(lambda s: list(map(lambda s: int(s), s.split(','))), line.strip('\n').split(' -> ')))
        if ends[0][0] == ends[1][0] or ends[0][1] == ends[1][1]:
            if ends[0][0] == ends[1][0]:
                dif = min(ends[0][1], ends[1][1])
                for i in range(abs(ends[0][1] - ends[1][1])+1):
                    if [ends[0][0], i+dif] not in positions:
                        positions.append([ends[0][0], i+dif])
                    else:
                        if [ends[0][0], i+dif] not in doublePositions:
                            doublePositions.append([ends[0][0], i+dif])
            else:
                dif = min(ends[0][0], ends[1][0])
                for i in range(abs(ends[0][0] - ends[1][0])+1):
                    if [i+dif, ends[1][1]] not in positions:
                        positions.append([i+dif, ends[1][1]])
                    else:
                        if [i+dif, ends[1][1]] not in doublePositions:
                            doublePositions.append([i+dif, ends[1][1]])
    print(len(doublePositions))

    #part2
    positions = []
    doublePositions = []
    for line in l:
        ends = list(map(lambda s: list(map(lambda s: int(s), s.split(','))), line.strip('\n').split(' -> ')))
        if ends[0][0] == ends[1][0] or ends[0][1] == ends[1][1]:
            if ends[0][0] == ends[1][0]:
                dif = min(ends[0][1], ends[1][1])
                for i in range(abs(ends[0][1] - ends[1][1])+1):
                    if [ends[0][0], i+dif] not in positions:
                        positions.append([ends[0][0], i+dif])
                    else:
                        if [ends[0][0], i+dif] not in doublePositions:
                            doublePositions.append([ends[0][0], i+dif])
            else:
                dif = min(ends[0][0], ends[1][0])
                for i in range(abs(ends[0][0] - ends[1][0])+1):
                    if [i+dif, ends[1][1]] not in positions:
                        positions.append([i+dif, ends[1][1]])
                    else:
                        if [i+dif, ends[1][1]] not in doublePositions:
                            doublePositions.append([i+dif, ends[1][1]])
        elif ends[0][0] == ends[0][1] and ends[1][0] == ends[1][1]:
            dif = min(ends[0][0], ends[1][0])
            for i in range(abs(ends[0][0] - ends[1][0])+1):
                if [i+dif, i+dif] not in positions:
                    positions.append([i+dif, i+dif])
                else:
                    if [i+dif, i+dif] not in doublePositions:
                        doublePositions.append([i+dif, i+dif])
        elif abs(ends[0][0]-ends[1][0]) == abs(ends[0][1]-ends[1][1]):
            dif = min(ends[0][0], ends[1][0])
            if ends[0][0]-ends[1][0] >= 0 and ends[0][1]-ends[1][1] >= 0:
                for i in range(ends[0][0]-ends[1][0]+1):
                    if [ends[0][0]-i, ends[0][1]-i] not in positions:
                        positions.append([ends[0][0]-i, ends[0][1]-i])
                    else:
                        if [ends[0][0]-i, ends[0][1]-i] not in doublePositions:
                            doublePositions.append([ends[0][0]-i, ends[0][1]-i])
            elif ends[0][0]-ends[1][0] < 0 and ends[0][1]-ends[1][1] < 0:
                for i in range(ends[1][0]-ends[0][0]+1):
                    if [ends[1][0]-i, ends[1][1]-i] not in positions:
                        positions.append([ends[1][0]-i, ends[1][1]-i])
                    else:
                        if [ends[1][0]-i, ends[1][1]-i] not in doublePositions:
                            doublePositions.append([ends[1][0]-i, ends[1][1]-i])
            elif ends[0][0]-ends[1][0] < 0 and ends[0][1]-ends[1][1] > 0:
                for i in range(ends[0][1]-ends[1][1]+1):
                    if [ends[1][0]-i, ends[1][1]+i] not in positions:
                        positions.append([ends[1][0]-i, ends[1][1]+i])
                    else:
                        if [ends[1][0]-i, ends[1][1]+i] not in doublePositions:
                            doublePositions.append([ends[1][0]-i, ends[1][1]+i])
            else:
                for i in range(ends[0][0]-ends[1][0]+1):
                    if [ends[1][0]+i, ends[1][1]-i] not in positions:
                        positions.append([ends[1][0]+i, ends[1][1]-i])
                    else:
                        if [ends[1][0]+i, ends[1][1]-i] not in doublePositions:
                            doublePositions.append([ends[1][0]+i, ends[1][1]-i])
    print(len(doublePositions))
