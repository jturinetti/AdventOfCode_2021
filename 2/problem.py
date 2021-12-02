def readInput(fileName):
        inputFile = open(fileName, 'r')
        return inputFile.readlines()

input = readInput('input.txt')

def problem1():
    horizontal = 0
    vertical = 0
    for entry in input:
        entryArr = entry.split(" ")
        command = entryArr[0]

        val = int(entryArr[1])
            
        if (command == 'forward'):
            horizontal = horizontal + val
        if (command == 'up'):
            vertical = vertical - val
        if (command == 'down'):
            vertical = vertical + val
    print(horizontal)
    print(vertical)
    return horizontal * vertical

def problem2():
    horizontal = 0
    vertical = 0
    aim = 0
    for entry in input:
        entryArr = entry.split(" ")
        command = entryArr[0]
        val = int(entryArr[1])
           
        if (command == 'forward'):
            horizontal = horizontal + val
            vertical = vertical + (aim * val)
        if (command == 'up'):
            aim = aim - val
        if (command == 'down'):
            aim = aim + val

    print(horizontal)
    print(vertical)
    print(aim)

    return horizontal * vertical

print(problem1())
print(problem2())