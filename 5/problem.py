class Line:
    def __init__(self, point1_x, point1_y, point2_x, point2_y):
        self.point1 = (point1_x, point1_y)
        self.point2 = (point2_x, point2_y)
        self.isstraight = (point1_x == point2_x) or (point1_y == point2_y)

def readandparseinput(fileName):
    inputFile = open(fileName, 'r')
    lines = []
    for line in inputFile.readlines():
        coords = line.split(' -> ')
        point1 = coords[0].split(',')
        point2 = coords[1].split(',')
        lines.append(Line(int(point1[0]), int(point1[1]), int(point2[0]), int(point2[1])))
    return lines

def drawhorizontalline(map, line):
    newintersections = 0
    incrementer = 1 if line.point1[0] < line.point2[0] else -1
    traveling_x = line.point1[0]
    while traveling_x != line.point2[0]:
        map[traveling_x][line.point1[1]] += 1
        if map[traveling_x][line.point1[1]] == 2:
            newintersections += 1
        
        traveling_x += incrementer
    
    map[traveling_x][line.point1[1]] += 1
    if map[traveling_x][line.point1[1]] == 2:
        newintersections += 1

    # print(f'drew horizontal line of length {abs(traveling_x - line.point1[0])} from {line.point1} to {line.point2}.  newintersections: {newintersections}') 
    return newintersections

def drawverticalline(map, line):
    newintersections = 0
    incrementer = 1 if line.point1[1] < line.point2[1] else -1
    traveling_y = line.point1[1]
    while traveling_y != line.point2[1]:
        map[line.point1[0]][traveling_y] += 1
        if map[line.point1[0]][traveling_y] == 2:
            newintersections += 1
        
        traveling_y += incrementer

    map[line.point1[0]][traveling_y] += 1
    if map[line.point1[0]][traveling_y] == 2:
        newintersections += 1
    
    # print(f'drew vertical line of length {abs(traveling_y - line.point1[1])} from {line.point1} to {line.point2}.  newintersections: {newintersections}') 
    return newintersections

def drawdiagonalline(map, line):
    newintersections = 0
    incrementer_x = 1 if line.point1[0] < line.point2[0] else -1
    incrementer_y = 1 if line.point1[1] < line.point2[1] else -1
    traveling_x = line.point1[0]
    traveling_y = line.point1[1]
    while traveling_y != line.point2[1]:
        map[traveling_x][traveling_y] += 1
        if map[traveling_x][traveling_y] == 2:
            newintersections += 1
        
        traveling_y += incrementer_y
        traveling_x += incrementer_x

    map[traveling_x][traveling_y] += 1
    if map[traveling_x][traveling_y] == 2:
        newintersections += 1
    
    return newintersections
    
linelist = readandparseinput('input.txt')
ventmap = [[0] * 1000 for x in range(1000)]
intersectioncount = 0

# problem 1
for line in linelist:
    if line.isstraight:
        if line.point1[0] == line.point2[0]:
            # vertical line
            intersectioncount += drawverticalline(ventmap, line)
        else:
            # horizontal line
            intersectioncount += drawhorizontalline(ventmap, line)

print(intersectioncount)

# reset data
ventmap = [[0] * 1000 for x in range(1000)]
intersectioncount = 0

#  problem 2
for line in linelist:
    if line.isstraight:
        if line.point1[0] == line.point2[0]:
            # vertical line
            intersectioncount += drawverticalline(ventmap, line)
        else:
            # horizontal line
            intersectioncount += drawhorizontalline(ventmap, line)
    else:
        # diagonal line
        intersectioncount += drawdiagonalline(ventmap, line)

print(intersectioncount)
