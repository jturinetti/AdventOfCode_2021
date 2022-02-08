#    a(0)
# b(1)     c(2)
#    d(3)
# e(4)     f(5)
#    g(6)   

# find 1, 4, 7, and 8
# c, f (which is which still unknown)

# determine top signal (7 chars - 1 chars)
# a

# determine middle signal (duplicate between 3 chars and 4 chars, minus c and f)
# d

# determine bottom signal (3 chars, the one we don't know)
# g

# determine bottom left signal (2 chars - the ones we know)
# e

# determine upper left signal (8 chars - the ones we know)
# b
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

    # array of strings that map to digits (digit is the index)
    # -1 indicates the signal string is not deduced yet
    digit_string_mapping = [-1] * 10
    
    # array of chars that map to signal position (index is the position (a = 0, b = 1, etc.))
    # -1 indicates the char is not deduced yet
    char_pos_mapping = [-1] * 10

    # loop over every line of input
    for line in inputarray:
        # loop through to find simple numbers first
        for signal_chars in line[0]:
            num = determine_number_simple(signal_chars)
            if (num > -1): digit_string_mapping[num] = ''.join(sorted(signal_chars))
        # upper and lower right signals
        char_pos_mapping[2] = digit_string_mapping[1][0]
        char_pos_mapping[5] = digit_string_mapping[1][1]
        # determine top signal (7 - 1)
        # digit_string_mapping[7] = 


        # FINALLY loop over 4 digits, create number, etc.
        str_num = ''
        for digit in line[1]:
            i = 0
            while i < len(digit_string_mapping):
                if digit_string_mapping[i] == digit:
                    str_num += str(i)
                i += 1
        # print(str_num)

    print(char_pos_mapping)
    print(digit_string_mapping)
    return

print(problem1())
print(problem2())