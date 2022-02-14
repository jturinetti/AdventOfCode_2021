#    a(0)
# b(1)     c(2)
#    d(3)
# e(4)     f(5)
#    g(6)   
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

def minus(first, second):
    result = []
    for c in first:
        if c not in second:
            result.append(c)
    return ''.join(sorted(result))

def minus_known_signals(num, known_signals):
    result = []
    for c in num:
        if c not in known_signals:
            result.append(c)
    return result

def intersection(first, second):
    result = []
    for c in first:
        if c in second:
            result.append(c)
    return ''.join(sorted(result))

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
    char_pos_mapping = [-1] * 7

    # loop over every line of input
    for line in inputarray:
        
        # loop through to find simple numbers first
        for signal_chars in line[0]:
            num = determine_number_simple(signal_chars)
            if (num > -1): digit_string_mapping[num] = ''.join(sorted(signal_chars))
        
        # upper and lower right signals, could be switched but doesn't matter
        char_pos_mapping[2] = digit_string_mapping[1][0]
        char_pos_mapping[5] = digit_string_mapping[1][1]
        
        # determine top signal (7 - 1)
        char_pos_mapping[0] = minus(digit_string_mapping[7], digit_string_mapping[1])
        
        # scan length 5 numbers (2, 3, 5)
        for num in line[0]:
            num = ''.join(sorted(num))
            
            if (len(num) == 5):
                if (digit_string_mapping[1][0] in num and digit_string_mapping[1][1] in num):
                    # it's 3?
                    the_mapping = minus_known_signals(minus(num, digit_string_mapping[4]), char_pos_mapping)
                    if (len(the_mapping) == 1):
                        digit_string_mapping[3] = num
                        char_pos_mapping[6] = the_mapping[0]
                
        # scan them again now that we determined 3!
        for num in line[0]:
            num = ''.join(sorted(num))
            if (len(num) == 5 and digit_string_mapping[3] != -1):
                remaining_signal = minus(num, digit_string_mapping[3])
                if (len(remaining_signal) == 1):
                    if (remaining_signal in digit_string_mapping[4]):
                        # it's 5
                        digit_string_mapping[5] = num
                        char_pos_mapping[1] = remaining_signal
                    else:
                        # it's 2
                        digit_string_mapping[2] = num
                        char_pos_mapping[4] = remaining_signal

        # scan length 6 numbers (0, 6, 9), looking for 6
        for num in line[0]:
            num = ''.join(sorted(num))
            if (len(num) == 6):
                if (char_pos_mapping[4] != -1 and char_pos_mapping[4] in num and char_pos_mapping[2] != -1 and char_pos_mapping[2] not in num):
                    # it's 6?
                    the_mapping = minus_known_signals(num, char_pos_mapping)
                    if (len(the_mapping) == 1):
                        digit_string_mapping[6] = num
                        char_pos_mapping[3] = the_mapping[0]
                    break

        # all signals determined, set 0 and 9
        digit_string_mapping[0] = ''.join(sorted(char_pos_mapping[0] + char_pos_mapping[1] + char_pos_mapping[2] + char_pos_mapping[4] + char_pos_mapping[5] + char_pos_mapping[6]))
        digit_string_mapping[9] = ''.join(sorted(char_pos_mapping[0] + char_pos_mapping[1] + char_pos_mapping[2] + char_pos_mapping[3] + char_pos_mapping[5] + char_pos_mapping[6]))

        # FINALLY loop over 4 digits, create number, etc.
        str_num = ''
        for digit in line[1]:
            # if (digit == ''): continue
            digit = ''.join(sorted(digit))
            i = 0
            while i < len(digit_string_mapping):
                if digit_string_mapping[i] == digit:
                    str_num += str(i)
                i += 1
        if (str_num != ''):
            running_total = running_total + int(str_num)
            # print(str_num)
            # print(running_total)

    # print(char_pos_mapping)
    # print(digit_string_mapping)
    return running_total

print(problem1())
print(problem2())