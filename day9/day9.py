if __name__ == '__main__':
    with open('day9challengefile.txt', 'r') as f:
        l = f.readlines()
    InpRows = list(map(lambda s: s.strip('\n'), l))
    rows = []
    for InpRow in InpRows:
        row = []
        for height in InpRow:
            row.append(int(height))
        rows.append(row)
    #part1
    result = 0
    rowCount = 0
    heightCount = 0
    for height in rows[0]:
        if heightCount == 0:
            if height < rows[0][1] and height < rows[1][0]:
                result += height+1
        elif heightCount == len(rows[0])-1:
            if height < rows[0][heightCount-1] and height < rows[1][heightCount]:
                result += height+1
        else:
            if height < rows[0][heightCount-1] and height < rows[0][heightCount+1] and height < rows[1][heightCount]:
                result += height+1
        heightCount += 1

    rowCount = 1
    for row in rows[1:-1]:
        heightCount = 0
        for height in row:
            if heightCount == 0:
                if height < row[1] and height < rows[rowCount-1][0] and height < rows[rowCount+1][0]:
                    result += height+1
            elif heightCount == len(row)-1:
                if height < row[heightCount-1] and height < rows[rowCount-1][heightCount] and height < rows[rowCount+1][heightCount]:
                    result += height+1
            else:
                if height < row[heightCount-1] and height < row[heightCount+1] and height < rows[rowCount-1][heightCount] and height < rows[rowCount+1][heightCount]:
                    result += height+1
            heightCount += 1
        rowCount += 1

    heightCount = 0
    for height in rows[rowCount]:
        if heightCount == 0:
            if height < rows[rowCount][1] and height < rows[rowCount-1][0]:
                result += height+1
        elif heightCount == len(rows[0])-1:
            if height < rows[rowCount][heightCount-1] and height < rows[rowCount-1][heightCount]:
                result += height+1
        else:
            if height < rows[rowCount][heightCount-1] and height < rows[rowCount][heightCount+1] and height < rows[rowCount-1][heightCount]:
                result += height+1
        heightCount += 1
    print(result)

    #part2
                    #  row
    def checkForBasin(x: int, y: int, rows: list, alreadyfound = [], depth = 0) -> list:
        if depth == 0:
            alreadyfound = []
        if x < 0:
            return alreadyfound
        if y < 0:
            return alreadyfound
        alreadyfound.append((x, y))
        try:
            if rows[x][y+1] != 9 and (x, y+1) not in alreadyfound:
                newRes = checkForBasin(x, y+1, rows, alreadyfound, depth +1)
                for res in newRes:
                    if res not in alreadyfound:
                        alreadyfound.append(res)
        except IndexError:
            pass
        try:
            if rows[x][y-1] != 9 and (x, y-1) not in alreadyfound:
                newRes = checkForBasin(x, y-1, rows, alreadyfound, depth +1)
                for res in newRes:
                    if res not in alreadyfound:
                        alreadyfound.append(res)
        except IndexError:
            pass
        try:
            if rows[x+1][y] != 9 and (x+1, y) not in alreadyfound:
                newRes = checkForBasin(x+1, y, rows, alreadyfound, depth +1)
                for res in newRes:
                    if res not in alreadyfound:
                        alreadyfound.append(res)
        except IndexError:
            pass
        try:
            if rows[x-1][y] != 9 and (x-1, y) not in alreadyfound:
                newRes = checkForBasin(x-1, y, rows, alreadyfound, depth +1)
                for res in newRes:
                    if res not in alreadyfound:
                        alreadyfound.append(res)
        except IndexError:
            pass
        result2 = []
        for pos in alreadyfound:
            if pos not in result2 and pos[0] >= 0 and pos[1] >= 0 and rows[pos[0]][pos[1]] != 9:
                result2.append(pos)
        return result2

    result = []
    rowCount = 0
    heightCount = 0
    for height in rows[0]:
        if heightCount == 0:
            if height < rows[0][1] and height < rows[1][0]:
                result.append(len(checkForBasin(rowCount, heightCount, rows)))
        elif heightCount == len(rows[0])-1:
            if height < rows[0][heightCount-1] and height < rows[1][heightCount]:
                result.append(len(checkForBasin(rowCount, heightCount, rows)))
        else:
            if height < rows[0][heightCount-1] and height < rows[0][heightCount+1] and height < rows[1][heightCount]:
                result.append(len(checkForBasin(rowCount, heightCount, rows)))
        heightCount += 1

    rowCount = 1
    for row in rows[1:-1]:
        heightCount = 0
        for height in row:
            if heightCount == 0:
                if height < row[1] and height < rows[rowCount-1][0] and height < rows[rowCount+1][0]:
                    result.append(len(checkForBasin(rowCount, heightCount, rows)))
            elif heightCount == len(row)-1:
                if height < row[heightCount-1] and height < rows[rowCount-1][heightCount] and height < rows[rowCount+1][heightCount]:
                    result.append(len(checkForBasin(rowCount, heightCount, rows)))
            else:
                if height < row[heightCount-1] and height < row[heightCount+1] and height < rows[rowCount-1][heightCount] and height < rows[rowCount+1][heightCount]:
                    result.append(len(checkForBasin(rowCount, heightCount, rows)))
            heightCount += 1
        rowCount += 1

    heightCount = 0
    for height in rows[rowCount]:
        if heightCount == 0:
            if height < rows[rowCount][1] and height < rows[rowCount-1][0]:
                result.append(len(checkForBasin(rowCount, heightCount, rows)))
        elif heightCount == len(rows[0])-1:
            if height < rows[rowCount][heightCount-1] and height < rows[rowCount-1][heightCount]:
                result.append(len(checkForBasin(rowCount, heightCount, rows)))
        else:
            if height < rows[rowCount][heightCount-1] and height < rows[rowCount][heightCount+1] and height < rows[rowCount-1][heightCount]:
                result.append(len(checkForBasin(rowCount, heightCount, rows)))
        heightCount += 1
    result.sort(reverse=True)
    print(result[0]*result[1]*result[2])
