import math
inf = math.inf


# Assumptions
# Implementation of the recursive Minimax algorithm to play tic tac toe
# crosses always play first and opponent/user is noughts

x = 'x'
o = 'o'


player = x
opponent = o

b = [
	[x,x,o],
	[o,0,0],
	[o,0,x]
]


row1 = [(0,0), (0,1), (0,2)]
row2 = [(1,0), (1,1), (1,2)]
row3 = [(2,0), (2,1), (2,2)]
rows = [row1,row2,row3]

col1 = [(0,0), (1,0), (2,0)]
col2 = [(0,1), (1,1), (2,1)]
col3 = [(0,2), (1,2), (2,2)]
cols = [col1,col2,col3]

diag1 = [(0,0),(1,1),(2,2)]
diag2 = [(0,2),(1,1),(2,0)]
diags = [diag1, diag2]

# Assumption: crosses always play first

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
# print (isValidBoard(b))
					 

def isMoveLeft(b):
	for i in range(3):
		for j in range(3):
			if b[i][j] == 0 :
				return True
	return False

# print(isMoveLeft(b))


def utilityValue(b):
    # row win
    for i in range(3):
        if (b[i][0]== b[i][1]):
            if (b[i][1]==b[i][2]):
                if b[i][2] == x:
                	print("row win")
                	return 100
                elif b[i][2] == o:
                	print("opponnent row win")
                	return -100

    # column win
    for j in range(3):
        if ((b[0][j]==b[1][j]) and (b[1][j]==b[2][j])):
            if b[1][j] == x:
                print("col win")
                return 100
            elif b[1][j] == o :
            	print("opponent col win")
            	return -100

    # diag win
    if (((b[0][0] == b[1][1]) and (b[1][1]==b[2][2])) or ((b[0][2]==b[1][1]) and (b[1][1]==b[2][0]))):
        if b[1][1] == x:
            print("diag win")
            return 100
        elif b[1][1] == o:
        	print("opponent diag win")
        	return -100
    return 0	


# print(utilityValue(b))

# now we write the recursive minimax function

def complementSymbol(symbol):
	if symbol == x:
		return o
	return x

def minimax(b, depth, symbol):
	nodeval = utilityValue(b)
	# check for cross win
	if nodeval == 100:
		return nodeval

	# check for nought win 
	if nodeval == -100:
		return nodeval

	# if neither has won, confirm that its a tie if no moves are left
	if isMoveLeft(b) == False:
		return 0

	if symbol == x :
		best = -inf

		for i in range(3):
			for j in range(3):
				# check if the location i,j is empty
				if b[i][j] == 0 :
					# play the hypothetical move
					b[i][j] = player

					print('max player')


					# call the minimax function again for the opponents turn to continue the game till the end
					best = max(best, minimax(b, depth + 1, complementSymbol(symbol) ))
					# undo the hypothetical move
					b[i][j] = 0

		return best

	if symbol== o :
		best = inf

		for i in range(3):
			for j in range(3):
				# check if the location is empty
				if b[i][j] == 0 :
					# play the hypothetical move
					b[i][j] = opponent 

					print('min player')

					best = min(best, minimax(b, depth + 1, complementSymbol(symbol)))

					b[i][j] = 0
		return best

# testing the minimax function

# finding the utility of the move of cross at 1,1

# b[0][1] = x
# print(b)
# MaxPlayer = True
# move_score = minimax(b, 0, False)
# print(move_score)
# print(b)

def bestMove(b):

	best_score = -inf
	row = -1
	col = -1

	for i in range(3):
		for j in range(3):
			if b[i][j] == 0 :
				
				b[i][j] = x
				move_score = minimax(b, 0, o)
				b[i][j] = 0

				if move_score > best_score :
					best_score = move_score
					row = i
					col = j


	print('the best move has utility',best_score)

	return best_score, row, col

# print('the utility value of the best move is:',bestMove(b))
# print('the best move position is:',row, col)	



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

def playMove(b, row, col, symbol):
    b[row][col] = symbol
    return
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
	# score,i,j = bestMove(b)
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
			score, i, j = bestMove(b)
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







		




















				



