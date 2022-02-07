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

def determine_number_simple(signal):
    if is_one(signal): return 1
    if is_four(signal): return 4
    if is_seven(signal): return 7
    if is_eight(signal): return 8
    return -1

def determine_number_advanced(signal):
    # TODO
    return -1

def determine_number(signal):
    num = -1
    # check 1, 4, 7, 8 first
    num = determine_number_simple(signal)
    if (num > -1): return num

    # power of deduction!
    return determine_number_advanced(signal)

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
    inputarray = parseinput(input)
    running_total = 0
    char_signal_mapping = [-1] * 10     # -1 indicates the signal string is not deduced yet
    print(char_signal_mapping)

    # loop over every line of input
    for line in inputarray:
        # loop through to find simple numbers first
        for signal_chars in line[0]:
            num = determine_number_simple(signal_chars)
            if (num > -1): char_signal_mapping[num] = ''.join(sorted(signal_chars))
        # loop again to see what we can determine
        

    print(char_signal_mapping)
    return

print(problem1())
print(problem2())