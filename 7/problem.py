def readinput(filename):
        inputfile = open(filename, 'r')
        return list(map(lambda x : int(x), inputfile.readline().split(',')))

input = readinput('input.txt')
input.sort()

# find median
def problem1():
    alignment_point = (int(len(input) / 2))
    print(alignment_point)
    alignment_val = input[alignment_point]
    fuel_required = 0
    for i in input:
        fuel_required += abs(i - alignment_val)
    return fuel_required

# find average
def problem2():
    avg = sum(input) / (int(len(input)))
    diff = -1
    prev_diff = 0
    index = 0
    while index < len(input):
        prev_diff = diff
        diff = input[index] - avg
        if diff >= 0: break
        index += 1
    selected_index = index
    if input[index] - avg > abs(prev_diff):
        selected_index = index - 1
    
    print(selected_index)
    print(input[selected_index])

    fuel_required = 0
    for i in input:
        n = abs(i - selected_index)
        fuel_required += (n^2 + n) / 2
        print(fuel_required)
    return fuel_required

print(problem1())
print(problem2())