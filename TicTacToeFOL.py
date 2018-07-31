import math

# This is an implementation of Tic Tac Toe player using Newell and Simon's strategy of playing tic tac toe based on First Order Logic

x = 'x'
o = 'o'
player = x
opponent = o

# we assume that the player x plays first and he is the computer, who is trying to win. The program is written for X to never lose
b = [
    [0,0,x],
    [o,x,0],
    [o,0,0]
]

def isMoveLeft(b):
	for i in range(3):
		for j in range(3):
			if b[i][j] == 0 :
				return True
	return False

print(isMoveLeft(b))

def isValidBoard(b):
	crosses = 0
	noughts = 0
	for i in range(3):
		for j in range(3):
			if b[i][j] == x :
				crosses = crosses + 1
			elif b[i][j] == o :
				noughts = noughts + 1
	if crosses >= noughts :
		return True
	return False
print (isValidBoard(b))

def playMove(b, row, col, symbol):
    b[row][col] = symbol
    return

# symbol denotes either cross or nought ie player or opponent
def checkWin(b, symbol):
    # row win
    for i in range(3):
        if (b[i][0]== b[i][1]):
            if (b[i][1]==b[i][2]):
                if b[i][2] == symbol:
                    
                    print("row win")
                    return True

    # column win
    for j in range(3):
        if ((b[0][j]==b[1][j]) and (b[1][j]==b[2][j])):
            if b[1][j] == symbol:
                print("col win")
                return True

    # diag win
    if (((b[0][0] == b[1][1]) and (b[1][1]==b[2][2])) or ((b[0][2]==b[1][1]) and (b[1][1]==b[2][0]))):
        if b[1][1] == symbol:
            print("diag win")
            return True
    return False

def complementSymbol(symbol):
	if symbol == 'x':
		return 'o'
	return 'x'

def OneMoveWinX(b):
    for i in range(3):
        for j in range(3):
            if (b[i][j]==0):
                b[i][j] = x
                if checkWin(b, player):
                    print("the win pos is",i,j)
                    b[i][j] = 0
                    return i,j
                b[i][j] = 0
    return -1,-1

def OneMoveWinO(b):
    for i in range(3):
        for j in range(3):
            if (b[i][j]==0):
                b[i][j] = o
                if checkWin(b, o):
                    print("the win pos is",i,j)
                    b[i][j] = 0
                    return i,j
                b[i][j] = 0
    return -1,-1

def TwoMoveWinX(b, symbol):
    if symbol == player:
        for i in range(3):
            for j in range(3):
                if b[i][j]==0:
                    b[i][j] = player
                    if checkWin(b, player):
                        b[i][j]= 0
                        return True
                    b[i][j] = 0
        return False
    # Here we want to check that the player wins no matter where the opponent plays
    if symbol == opponent:
        temp = True
        for i in range(3):
            for j in range(3):
                if b[i][j]==0:
                    b[i][j]=opponent
                    if checkWin(b, opponent):
                        temp = False
                    else:
                        temp = (temp) and (TwoMoveWinX(b,player))
                    b[i][j] = 0
        return temp

def playMoveTwo(b):
    for i in range(3):
        for j in range(3):
            if b[i][j]==0:
                b[i][j] == player
                if TwoMoveWinX(b, opponent):
                    b[i][j] = 0
                    print("the two move win vals are",i,j)
                    return i,j
                b[i][j] = 0
    return -1, -1

def ThreeMoveWin(b, symbol):
    if symbol == player :
        for i in range(3):
            for j in range(3):
                if b[i][j]==0:
                    b[i][j] == player
                    if TwoMoveWinX(b,opponent):
                        b[i][j] = 0
                        return True
                    b[i][j] = 0
        return False
    if symbol == opponent:
        temp = True
        for i in range(3):
            for j in range(3):
                if b[i][j] == 0:
                    b[i][j] = opponent
                    temp = temp and ThreeMoveWin(b,player)
                    b[i][j]=0
        return temp

def playMoveThree(b):
	for i in range(3):
	    for j in range(3):
	    	if b[i][j] == 0:
	    		b[i][j] = player
	    		if ThreeMoveWin(b, opponent):
	    			b[i][j] = 0
	    			print("the three move win vals are",i,j)
	    			return i, j
	    		b[i][j] = 0
	return -1,-1

def arbitraryMove(b, symbol):
    if b[1][1] == 0:
        b[1][1] = symbol
        return 1,1
    else:
        for i in range(3):
            for j in range(3):
                if b[i][j] == 0:
                    b[i][j] = symbol
                    return i,j


# now we call the above functions in a particular order to implement our strategy
# print(b)
def getBestMove(b, symbol):
    if isValidBoard(b):
        if checkWin(b, player):
            print("x wins")
            return
        elif checkWin(b, opponent):
            print("o wins")
            return
        elif not isMoveLeft(b):
            print("its a draw")
            return

        row = -1
        col = -1    
        
        row , col = OneMoveWinX(b)
        if row != -1:
            print("one move win x")
            return row, col
        row, col = OneMoveWinO(b)
        if row != -1:
            print("one move win o")
            return row, col
        row, col = playMoveTwo(b)
        if row != -1:
            print("play move two")
            return row, col
        row, col = playMoveThree(b)
        if row != -1:
            print("play move three")
            return row, col
        row, col = arbitraryMove(b,player)
        print("arbitrary move")
        return row, col

print("The best move for the given board is ", getBestMove(b, player))
# print(OneMoveWinX(b))



def printBoard(b):
    print(b[0][0],b[0][1],b[0][2])
    print(b[1][0],b[1][1],b[1][2])
    print(b[2][0],b[2][1],b[2][2])
    return



#  the computer is cross and the user is noughts, the computer always plays first
def playWithUser():
    b = [[x,0,0]
        ,[0,0,0]
        ,[0,0,0]]


    #play the first move 
    # i,j = getBestMove(b,player)
    # playMove(b,i,j,player)
    printBoard(b)

    while(isMoveLeft(b)):
        # take input from user for his move
        temp1 = input('Enter row move: ')
        temp2 = input('Enter col move: ')
        row = int(temp1)
        col = int(temp2)

        playMove(b, row, col, opponent)
        printBoard(b)

        if checkWin(b,player):
            print('Computer wins')
            return
        if checkWin(b, opponent):
            print('User wins')
            return

        if isMoveLeft(b):
            i, j = getBestMove(b,player)
            playMove(b,i,j,player)
            printBoard(b)   
            if checkWin(b,player):
                print('Computer wins')
                return
            if checkWin(b, opponent):
                print('User wins')
                return
    if (not isMoveLeft(b)):
        print('Tie')
        return

playWithUser()





























            



















