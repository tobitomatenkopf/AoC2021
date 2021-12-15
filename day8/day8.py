if __name__ == '__main__':
    with open('day8challengefile.txt', 'r') as f:
        l = f.readlines()
    #part1
    digits = []
    amount = 0
    for line in l:
        for numb in line.strip('\n').split(' | ')[1].split(' '):
            digits.append(numb)
    for digit in digits:
       if 2 <= len(digit) <= 4:
            amount += 1
        if len(digit) == 7:
            amount += 1
    print(amount)

    #part2
    with open('day8challengefile.txt', 'r') as f:
        l = f.readlines()
    sum = 0
    for line in l:
        frontPart = line.split(' | ')[0].split(' ')
        allChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        charPosis = ['', '', '', '', '', '', '']
        encrypted = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for digit in frontPart:
            if 2 == len(digit):
                encrypted[1] = digit
            elif len(digit) == 3:
                encrypted[7] = digit
            elif len(digit) == 4:
                encrypted[4] = digit
            elif len(digit) == 7:
                encrypted[8] = digit
        for char in encrypted[7]:
            if char not in encrypted[1]:
                charPosis[0] = char
                break
        for digit in frontPart:
            if len(digit) == 5:
                if encrypted[7][0] in digit and encrypted[7][1] in digit and encrypted[7][2] in digit:
                    encrypted[3] = digit
        for char in encrypted[4]:
            if char not in encrypted[3]:
                charPosis[1] = char
                break
        for char in encrypted[4]:
            if char not in encrypted[1] and char != charPosis[1]:
                charPosis[3] = char
                break
        for char in allChars:
            if char not in encrypted[3] and char not in charPosis:
                charPosis[4] = char
                break
        for char in allChars:
            if char not in encrypted[1] and char not in charPosis:
                charPosis[6] = char
                break
        for digit in frontPart:
            if len(digit) == 5 and charPosis[4] not in digit and charPosis[1] in digit:
                encrypted[5] = digit
                break
        for char in allChars:
            if char not in charPosis and char not in encrypted[5]:
                charPosis[2] = char
                break
        for char in allChars:
            if char not in charPosis:
                charPosis[5] = char
                break

        backPart = frontPart = line.split(' | ')[1].strip('\n').split(' ')
        result = []
        for digit in backPart:
            if len(digit) == 2:
                result.append('1')
            elif len(digit) == 3:
                result.append('7')
            elif len(digit) == 4:
                result.append('4')
            elif len(digit) == 5:
                if charPosis[4] in digit:
                    result.append('2')
                elif charPosis[1] in digit:
                    result.append('5')
                else:
                    result.append('3')
            elif len(digit) == 6:
                if charPosis[3] not in digit:
                    result.append('0')
                elif charPosis[4] in digit:
                    result.append('6')
                else:
                    result.append('9')
            else:
                result.append('8')
        sum += int(''.join(result))
print(sum)
