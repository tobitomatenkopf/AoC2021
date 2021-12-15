from timeit import timeit


if __name__ == '__main__':
    with open('day6challengefile.txt', 'r') as f:
        l = f.readlines()
    numbers = list(map(lambda s: int(s), l[0].strip('\n').split(',')))
    newnumbers = []
    additions = []
    for i in range(80):
        for numb in numbers:
            if numb == 1:
                newnumbers.append(0)
            elif numb == 0:
                newnumbers.append(6)
                additions.append(8)
            else:
                newnumbers.append(numb-1)
        numbers = newnumbers
        for add in additions:
            numbers.append(add)
        newnumbers = []
        additions = []
    print(len(numbers))

    with open('day6challengefile.txt', 'r') as f:
        l = f.readlines()
    numbers = list(map(lambda s: int(s), l[0].strip('\n').split(',')))
    newnumbs = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for numb in numbers:
        newnumbs[numb-1] += 1
    newnumbers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(255):
        for numb in range(9):
            if numb == 0:
                newnumbers[8] += newnumbs[0]
                newnumbers[6] += newnumbs[0]
            else:
                newnumbers[numb-1] += newnumbs[numb]
        newnumbs = newnumbers
        newnumbers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    res = 0
    for elem in newnumbs:
        res += elem
    print(res)
