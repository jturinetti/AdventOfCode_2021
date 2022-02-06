def readInput(fileName):
        inputFile = open(fileName, 'r')
        return inputFile.readlines()


input = readInput('input.txt')


def parseinput(input):
    inputarray = []
    for line in input:
        clues_and_number = line.rstrip().split('|')
        clues = [x for x in clues_and_number[0].split(' ') if x != '']
        number = [x for x in clues_and_number[1].split(' ') if x != '']
        inputarray.append((clues, number))
    return inputarray

def is_one(signal):
    return len(signal) == 2

def is_four(signal):
    return len(signal) == 4

def is_seven(signal):
    return len(signal) == 3

def is_eight(signal):
    return len(signal) == 7

def problem1():
    inputarray = parseinput(input)
    appearancecount = 0
    for line in inputarray:
        for digit in line[1]:
            if is_one(digit): appearancecount += 1
            if is_four(digit): appearancecount += 1
            if is_seven(digit): appearancecount += 1
            if is_eight(digit): appearancecount += 1

    return appearancecount

def problem2():
    # TODO
    return

print(problem1())
# print(problem2())