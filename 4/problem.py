class Bingo:
    def __init__(self, bingoseq):
        self.bingosequence = bingoseq
        # print(self.bingosequence)
        self.bingoboards = []
        self.numberindex = 0
        self.wonboards = []
    
    def addbingoboard(self, board):
        # print(board)
        self.bingoboards.append(board)
        
    def callnumber(self):
        # initialize
        if self.wonboards == []:
            self.wonboards = [0] * len(self.bingoboards)

        callednumber = self.bingosequence[self.numberindex]
        print(callednumber)
        for bindex in range(len(self.bingoboards)):
            b = self.bingoboards[bindex]
            updatedcoords = self.__markboard__(b, callednumber)
            # print(updatedcoords)
            if self.wonboards[bindex] == 0 and self.__checkboard__(b, updatedcoords):
                # problem 1
                # return self.__unmarkedsum__(b) * callednumber
                # problem 2
                self.wonboards[bindex] = self.__unmarkedsum__(b) * callednumber
                print(self.wonboards)
                if all(n > 0 for n in self.wonboards):
                    return self.wonboards[bindex]
        print('all boards marked, calling next number')
        self.numberindex += 1
        return 0

    def __markboard__(self, board, number):
        updatedcoords = []
        # print(board)
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col][0] == number:
                    board[row][col] = (number, True)
                    print('board updated!')
                    # print(row)
                    # print(col)
                    # print(board[row][col])
                    updatedcoords.append((row, col))
        return updatedcoords

    def __checkboard__(self, board, updatedcoords):
        for coord in updatedcoords:
            if self.__checkboardrow(board, coord[0]) or self.__checkboardcol(board, coord[1]):
                return True

        return False

    def __checkboardrow(self, board, rowindex):
        return board[rowindex][0][1] and board[rowindex][1][1] and board[rowindex][2][1] and board[rowindex][3][1] and board[rowindex][4][1]

    def __checkboardcol(self, board, colindex):
        return board[0][colindex][1] and board[1][colindex][1] and board[2][colindex][1] and board[3][colindex][1] and board[4][colindex][1]

    def __unmarkedsum__(self, board):
        sum = 0
        for row in board:
            for x in row:
                if x[1] == False:
                    sum += x[0]
        return sum

def readandparseinput(filename):
    with open(filename) as file:
        bingo = Bingo(list(map(lambda n: int(n), file.readline().split(','))))
        line = file.readline()
        
        boardrows = []

        while line:
            line = file.readline()
            if line not in ('\n', '\r\n'):
                bingorow = list(map(lambda n: (int(n), False), list(filter(None, line.split(' ')))))
                boardrows.append(bingorow)
            else:
                bingo.addbingoboard(boardrows)
                boardrows = []
        return bingo

# problem 2
bingo = readandparseinput('input.txt')
solution = 0
while solution == 0:
    solution = bingo.callnumber()
else:
    print(solution)

