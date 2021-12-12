def readinput(fileName):
        inputfile = open(fileName, 'r')
        return list(map(lambda x : int(x), inputfile.readline().split(',')))

input = readinput('input.txt')

# problem 1
fisharray = input
daycount = 80
week = 7
counter = week

while counter <= daycount:
    fisharray_temp = []
    for lf in fisharray:
        if lf >= week:
            fisharray_temp.append(lf - week)
        else:
            fisharray_temp.append(lf)
            fisharray_temp.append(lf + 2)
    fisharray = fisharray_temp
    # print(counter)
    # print(len(fisharray))
    counter += week

# handle remainder
remainder = daycount - (counter - week)
finalcount = len(fisharray)
for lf in fisharray:
    if lf < remainder:
        finalcount += 1

print(finalcount)