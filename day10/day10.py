import timeit

if __name__ == '__main__':
    with open('day10challengefile.txt') as f:
        l = f.readlines()

l = list(map(lambda s: s.strip('\n'), l))

def solve1():
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    points = [3, 57, 1197, 25137]
    score = 0
    for line in l:
        opend = []
        for bracket in line:
            if bracket in opening:
                opend.append(bracket)
            else:
                if opening.index(opend.pop()) != closing.index(bracket):
                    score += points[closing.index(bracket)]
                    break
    print(score)

solve1()

def solve2():
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    points = [1, 2, 3, 4]
    scores = []
    for line in l:
        opend = []
        corupted = False
        for bracket in line:
            if bracket in opening:
                opend.append(bracket)
            else:
                if opening.index(opend.pop()) != closing.index(bracket):
                    corupted = True
                    break
        if not corupted:
            opend.reverse()
            score = 0
            for bracket in opend:
                score = score*5 + points[opening.index(bracket)]
            scores.append(score)
    scores.sort()
    print(scores[int((len(scores)//2])

solve2()
