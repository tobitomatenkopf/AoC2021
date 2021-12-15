if __name__ == '__main__':
    with open('day7challengefile.txt', 'r') as f:
        l = f.readlines()
    positions = list(map(lambda s: int(s), l[0].strip('\n').split(',')))

    #part1
    minFuel = 0
    for align in range(max(positions)-min(positions)):
        fuelCost = 0
        for pos in positions:
            fuelCost += abs(align - pos)
        if minFuel != 0:
            minFuel = min(minFuel, fuelCost)
        else:
            minFuel = fuelCost
        fuelCost = 0

    print(minFuel)

    #part2
    minFuel = 0
    for align in range(max(positions)-min(positions)):
        fuelCost = 0
        for pos in positions:
            fuelCost += (abs(align - pos)*(abs(align - pos)+1))/2
        if minFuel != 0:
            minFuel = min(minFuel, fuelCost)
        else:
            minFuel = fuelCost
        fuelCost = 0

    print(str(minFuel).strip('.0'))
