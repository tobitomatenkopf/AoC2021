if __name__ == '__main__':
    with open('day7challengefile.txt', 'r') as f:
        l = f.readlines()
    positions = sorted(list(map(lambda s: int(s), l[0].strip('\n').split(','))))
    align = positions[int(len(positions)/2)]
    fuelCost = 0
    for pos in positions:
        fuelCost += abs(align - pos)
    print(fuelCost)
    fuelCost = 0
    for pos in positions:
        fuelCost += (abs(align - pos)*(abs(align - pos)+1))/2
    print(int(fuelCost))
