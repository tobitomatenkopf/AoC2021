def readFile():
    with open('day4challengefile.txt', 'r') as f:
        l = f.readlines()
        numbers = list(map(lambda s: int(s), l[0].strip('\n').split(',')))
        papers = []
        storage = []
        for line in l[2:]:
            if line != '\n':
                storage.append(list(map(lambda s: [int(s), False], line.strip('\n').split())))
            else:
                papers.append(storage)
                storage = []
        papers.append(storage)
        return numbers, papers


if __name__ == '__main__':
    #part1
    numbers, papers = readFile()
    breaking = False
    winningPaper = []
    lastNumb = 0
    for numb in numbers:
        for paper in papers:
            for row in paper:
                try:
                    row[row.index([numb, False])][1] = True
                except ValueError:
                    pass
                if row[0][1] == True and row[1][1] == True and row[2][1] == True and row[3][1] == True and row[4][1] == True:
                    winningPaper = paper
                    lastNumb = numb
                    breaking = True
                    break
            for i in range(5):
                if paper[0][i][1] == True and paper[1][i][1] == True and paper[2][i][1] == True and paper[3][i][1] == True and paper[4][i][1] == True:
                    winningPaper = paper
                    lastNumb = numb
                    breaking = True
                    break
            if breaking == True:
                break
        if breaking == True:
            break
    sum = 0
    for row in winningPaper:
        for numb in row:
            if numb[1] == False:
                sum += numb[0]
    print(sum*lastNumb)

    #part2
    numbers, papers = readFile()
    winningPapers = []
    isWinning = False
    breaking = False
    losingPaper = []
    for numb in numbers:
        paperNumb = 0
        for paper in papers:
            for row in paper:
                try:
                    row[row.index([numb, False])][1] = True
                except ValueError:
                    pass
                if row[0][1] == True and row[1][1] == True and row[2][1] == True and row[3][1] == True and row[4][1] == True:
                    isWinning = True
                    break
            for i in range(5):
                if paper[0][i][1] == True and paper[1][i][1] == True and paper[2][i][1] == True and paper[3][i][1] == True and paper[4][i][1] == True:
                    isWinning = True
                    break
            if isWinning:
                if paperNumb not in winningPapers:
                    winningPapers.append(paperNumb)
                isWinning = False
            paperNumb += 1
            if len(winningPapers) == len(papers):
                losingPaper = paper
                breaking = True
                lastNumb = numb
                break
        if breaking == True:
            break
        paperNumb = 0
    sum = 0
    for row in losingPaper:
        for numb in row:
            if numb[1] == False:
                sum += numb[0]
    print(sum*lastNumb)
