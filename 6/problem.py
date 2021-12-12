def readinput(fileName):
        inputfile = open(fileName, 'r')
        return list(map(lambda x : int(x), inputfile.readline().split(',')))

def lanternfish_brute_alg(filename, daycount):
    fisharray = readinput(filename)
    week = 7
    currentday = week

    while currentday <= daycount:
        print(currentday)
        fisharray_temp = []
        for lf in fisharray:
            if lf >= week:
                fisharray_temp.append(lf - week)
            else:
                fisharray_temp.append(lf)
                fisharray_temp.append(lf + 2)
        fisharray = fisharray_temp
        currentday += week
        print(f'lanternfish count: {len(fisharray)}')
    # handle remainder
    remainder = daycount - (currentday - week)
    finalcount = len(fisharray)
    for lf in fisharray:
        if lf < remainder:
            finalcount += 1

    print(f'final lanternfish count: {len(fisharray)}')
    return finalcount

def lanternfish_calculator(ttl, daysremaining):
    return

def lanternfish_alg_smart(filename, daycount):
    fisharray = readinput(filename)
    week = 7
    currentday = week

    # for each number, calculate total number of added lanternfish based on days remaining
    # WIP
    return

def problem1():
    return lanternfish_brute_alg('input.txt', 80)

def problem2():
    return lanternfish_brute_alg('test.txt', 256)


print(problem1())
print(problem2())