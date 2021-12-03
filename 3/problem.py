def readInput(fileName):
        inputFile = open(fileName, 'r')
        return inputFile.readlines()

input = readInput('input.txt')

def countbitsatindex(data, index, determiner):
    count = 0
    bin1arr, bin0arr = [], []
    for b in data:
        if b[index] == '1':
            count = count + 1
            bin1arr.append(b)
        else:
            bin0arr.append(b)
    
    halfwaypoint = len(data) / 2
    
    if count >= halfwaypoint:
        if determiner == 'most': return bin1arr 
        else: return bin0arr 
    else:
        if determiner == 'most': return bin0arr
        else: return bin1arr

def countallbits():
    countarray = [0] * 12
    for b in input:
        for i, ch in enumerate(b):
            if ch == '1':
                countarray[i] = countarray[i] + 1
    print(countarray)
    return countarray

def problem1():
    countarray = countallbits()
    halfwaypoint = len(input) / 2
    
    gammabinstr = '0b'
    epsilonbinstr = '0b'
    for count in countarray:
        gammabinstr += '1' if count >= halfwaypoint else '0'
        epsilonbinstr += '0' if count >= halfwaypoint else '1'

    print(gammabinstr)
    print(epsilonbinstr)

    return int(gammabinstr, 2) * int(epsilonbinstr, 2)

def problem2():
    data = input
    index = 0
    while (len(data) > 1):
        data = countbitsatindex(data, index, 'most')
        index += 1
    print(data)
    val1 = int(data[0], 2)
    data = input
    index = 0
    while (len(data) > 1):
        data = countbitsatindex(data, index, 'least')
        index += 1
    print(data)
    val2 = int(data[0], 2)
    return val1 * val2

print(problem1())
print(problem2())