### Trey Alexander ###

def spaceOpen(board, pos): # checks to see if the space is open or taken
    if board[pos] == ' ':
        return True 
    else:
        return False


def insertLetter(board, letter, pos): # inserts letter at position, unless taken.
    if spaceOpen(board, pos):
        board[pos] = letter 
        printBoard(board)
        if (drawState(board)):
            print ("Game ended: Draw")
            exit()
        elif validWinState(board):
            if playedWinState(board, "X"):
                print("Game ended: AI Wins")
                exit()
            else:
                print("Game ended: Human Wins")
                exit()
        
        return 

    else: # if taken, error
        print("That space is not open ")
        pos = int(input("Please make a new move: "))
        insertLetter(board, letter, pos)
        return


def printBoard(board): # prints board
    print("  |   |")
    print(board[1] + "   " + board[2] + "   " + board[3])
    print("  |   |")
    print(board[4] + "   " + board[5] + "   " + board[6])
    print("  |   |")
    print(board[7] + "   " + board[8] + "   " + board[9])
    print("  |   |")
    print("\n\n")

def validWinState(board): # checks to see if the state is 3 in a row
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '): # 1 2 3
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '): # 1 4 7
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '): # 1 5 9
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '): # 2 5 8
        return True
    elif (board[3] == board[5] and board[3] == board[7] and board[3] != ' '): # 3 5 7
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '): # 4 5 6
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '): # 7 8 9
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '): # 3 6 9
        return True
    else:
        return False

def playedWinState(board, pickedSpot): # checks to see if the chosen state is 3
    if (board[1] == board[2] and board[1] == board[3] and board[1] == pickedSpot # 1 2 3
    or board[1] == board[4] and board[1] == board[7] and board[1] == pickedSpot # 1 4 7
    or board[1] == board[5] and board[1] == board[9] and board[1] == pickedSpot # 1 5 9
    or board[2] == board[5] and board[1] == board[8] and board[2] == pickedSpot # 2 5 8
    or board[3] == board[5] and board[3] == board[7] and board[3] == pickedSpot # 3 5 7
    or board[4] == board[5] and board[4] == board[6] and board[4] == pickedSpot # 4 5 6
    or board[7] == board[8] and board[7] == board[9] and board[7] == pickedSpot # 7 8 9
    or board[3] == board[6] and board[3] == board[9] and board[3] == pickedSpot): # 3 6 9
        return True
    else:
        return False
    
    
def drawState(board): # In case of a draw
    for key in board.keys():
        if board[key] == ' ':
            return False
    
    return True 

def humanMove(human, board): # player movement
    pos = int(input("Your move, human! Enter for 'O': "))
    insertLetter(board, human, pos)
    return

def AIMove(board, AI, human): # AI movement
    bestScore = -10000
    bestMove = -10000

    for key in board.keys():
        if(board[key] == ' '):
            board[key] = AI 
            score = miniMax(board, False, AI, human)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score 
                bestMove = key
    
    insertLetter(board, AI, bestMove) # adds letter where declared
    return 

def miniMax(board, isMax, AI, human):
    
    if validWinState(board):
        return 1 # AI win

    elif validWinState(board):
        return -1 # player win
    
    elif drawState(board):
        return 0 # draw

    # determine who is playing
    if isMax:
        bestScore = 100

        for key in board.keys():
            if(board[key] == ' '):
                board[key] = AI 
                score = miniMax(board, False, AI, human) # signifies to play vs below else statement
                board[key] = ' '
                if (playedWinState, AI):
                    score = 1000
                    if (score < bestScore):
                        bestScore = score
                else:
                    score = -1000
                    if (score < bestScore):
                        bestScore = score


        return bestScore

    else: # skips to this as False case to play vs itself
        bestScore = -100

        for key in board.keys():
            if(board[key] == ' '):
                board[key] = human
                score = miniMax(board, True, AI, human) # signifies to play vs above if statement
                board[key] = ' '
                if (playedWinState, AI):
                    score = -1000
                    if (score < bestScore):
                        bestScore = score
                else:
                    score = -1000
                    if (score < bestScore):
                        bestScore = score

        return bestScore # plays vs itself repeatedly until win


def main():
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}


    human = 'O'
    AI = 'X'

    print("\n Tic Tac Toe Board:\n")
    printBoard(board)

    print("\n")


    while not validWinState(board):
        AIMove(board, AI, human)
        humanMove(human, board)

main()