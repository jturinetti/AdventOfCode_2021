def readInput(fileName):
        inputFile = open(fileName, 'r')
        return inputFile.readlines()

input = readInput('input.txt')

def problem1():
    countarray = [0] * 12
    for b in input:
        for i, ch in enumerate(b):
            if ch == '1':
                countarray[i] = countarray[i] + 1

    print(countarray)
    print(len(input))

    gammabinstr = '0b'
    epsilonbinstr = '0b'
    for count in countarray:
        gammabinstr += '1' if count >= 500 else '0'
        epsilonbinstr += '0' if count >= 500 else '1'

    print(gammabinstr)
    print(epsilonbinstr)

    return int(gammabinstr, 2) * int(epsilonbinstr, 2)

def problem2():
    return

print(problem1())
print(problem2())