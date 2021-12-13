def readinput(filename):
        inputfile = open(filename, 'r')
        return list(map(lambda x : int(x), inputfile.readline().split(',')))

input = readinput('input.txt')
input.sort()

def problem1():
    alignment_point = (int(len(input) / 2))
    print(alignment_point)
    alignment_val = input[alignment_point]
    fuel_required = 0
    for i in input:
        fuel_required += abs(i - alignment_val)
    return fuel_required

def problem2():
    # TODO
    return

print(problem1())
print(problem2())