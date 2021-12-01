def readInput(fileName):
        inputFile = open(fileName, 'r')
        return inputFile.readlines()

input = readInput('input.txt')

def problem1():
    increaseCount = 0
    for n in range(len(input)):
        if n > 0:
            if int(input[n]) > int(input[n-1]):
                increaseCount = increaseCount + 1
    return increaseCount

def problem2():
    increaseCount = 0
    for n in range(len(input)):
        if n > 2:
            if int(input[n]) > int(input[n-3]):
                increaseCount = increaseCount + 1
    return increaseCount

print(problem1())
print(problem2())