def readinput(fileName):
        inputfile = open(fileName, 'r')
        return list(map(lambda x : int(x), inputfile.readline().split(',')))

def lanternfish_brute_alg(filename, daycount):
    fisharray = readinput(filename)
    week = 7
    currentday = week

    while currentday <= daycount:
        fisharray_temp = []
        for lf in fisharray:
            if lf >= week:
                fisharray_temp.append(lf - week)
            else:
                fisharray_temp.append(lf)
                fisharray_temp.append(lf + 2)
        fisharray = fisharray_temp
        currentday += week
        
    # handle remainder
    remainder = daycount - (currentday - week)
    finalcount = len(fisharray)
    for lf in fisharray:
        if lf < remainder:
            finalcount += 1
    
    return finalcount

fib_cache = [0] * 256
fib_cache[0] = 1
fib_cache[1] = 1

def fib(n):
    if (n <= 1): return 1
    if fib_cache[n-1] == 0:
        fib1 = fib(n-1)
        fib_cache.insert(n-1, fib1)
        # print(f'inserting {n-1}, {fib1}')
    else: 
        fib1 = fib_cache[n-1]

    if fib_cache[n-2] == 0:
        fib2 = fib(n-2)
        fib_cache.insert(n-2, fib2)
        # print(f'inserting {n-2}, {fib2}')
    else:
        fib2 = fib_cache[n-2]

    return fib1 + fib2

def lanternfish_calculator(ttl, daysremaining):
    # fibonacci sequence + remainder func
    iterations = (int)(daysremaining / 7)
    remainder = daysremaining % 7
    
    return fib(iterations) + 1 if remainder > ttl else 0

def lanternfish_smart_alg(filename, daysremaining):
    fisharray = readinput(filename)
    totalcount = 0

    # for each number, calculate total number of added lanternfish based on days remaining
    for lf in fisharray:
        totalcount += 1 + lanternfish_calculator(lf, daysremaining)
    return totalcount

def problem1():
    return lanternfish_brute_alg('input.txt', 80)

def problem2():
    return lanternfish_smart_alg('test2.txt', 10)


print(problem1())
print(problem2())