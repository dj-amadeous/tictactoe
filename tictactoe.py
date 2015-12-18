#tic tac toe
import random
#prints board that it was passed
def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = raw_input('Do you want to be X or O?').upper()
    if letter == 'X':
    #I don't understand how the computer magically knows that the first input X is going to be the players letter
        return ['X','O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    #defines who goes first
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    #In this function, does python automatically interpret 'y' to be yes and then start the game over? wtf?
    return raw_input('Do you want to play again (yes or no?)').lower().startswith('y')

def makeMove(board, letter, move):
    #here the function accepts the board, move, and letter as arguments which will be called later in the gameplay function
    board[move] = letter

#checks current board for win
def isWinner(bo, le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or #across the bottom
            (bo[4] == le and bo[5] == le and bo[6] == le) or #across middle
            (bo[7] == le and bo[8] == le and bo[9] == le) or #across top
            (bo[7] == le and bo[4] == le and bo[1] == le) or #down left
            (bo[8] == le and bo[5] == le and bo[2] == le) or #down middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or #down right
            (bo[9] == le and bo[5] == le and bo[1] == le) or #diagonal right
            (bo[7] == le and bo[5] == le and bo[3] == le))


def getBoardCopy(board):
    dupeBoard = []
    #I say this every time I write a for statement, but what the hell does i stand for. I know it's a stand in variable
    #but for "what" in board, append "what"
    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    #Here I'm assuming that since board[move] is typed the same way as in the checkForWin function board[1] etc
    #Python magically knows that we're referencing that function, and also magically knows that ' ' stands for our "letter"
    # Return true if the passed move is free on the passed board. (thi sis the comment on the original program)
    #I also don't understand how python magically knows to return true if the move passed is free. Where is True referenced here?
    return board[move] == ' '

def getPlayerMove(board):
    #First we set move to empty
    move = ' '
    #then we say if move is not 1-9, or not free, ask again "what is your next move". Return the input
    #does return here mean that python is going to accept the input as replace the blank space on the board automatically?
    #or does that need to be specified later?
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        move = raw_input("What is your next move? (1-9)")
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    #where did movesList come from?
    #we set possibleMoves to an empty array
    possibleMoves = []
    for i in movesList:
    #then, if the space is free on the board for i in movesList(I'm assuming movesList is magically every possible move?)
    #we append that move to the array of possible moves
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    #if the total number of possible moves is NOT zero
    if len(possibleMoves) != 0:
        #return a random choice from the possibleMoves array
        return random.choice(possibleMoves)
    else:
        #if it IS zero, do nothing
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1,10):
        #On this line, we're using that function that I had a problem with earlier. reassigning getBoardCopy to just copy
        #then calling hte isSpaceFree function and passing it the duplicate board, and i as an argument. i in this instance
        #I know is the numbers 1 through 10 repeated. Thus it's like saying isSpaceFree 1, makeMove passing the board as an argument
        #the computers letter, and i(1 in this instance).

        copy = getBoardCopy(board)
        #here if the space is free, passing hte board, and the numbers 1-9 as an argument (that's what i is in this case)
        if isSpaceFree(copy,i):
            #call the make move function, arguments of the current board, with the computer letter, with the letters 1-9
            #If I understand this correctly, isn't the computer just going to pick each space on the board in order 1-9?
            makeMove(copy, computerLetter, i)
            #I'm under the impression that isWinner checks for a board ALREADY winning. However this if statement gives me
            #the impression that if isWinner(which in my head is a board already won) is out there, then return i which is
            #just hte next number in order 1-9???
            #I know that the if statement is TRYING To say to pick the square that would be the tictactoe knockout but
            #I don't get HOW it's saying that.
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            #all of my questions here are the same as above, since it's basically the same thing
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    #This one makes alot of sense, chooseRandomMoveFromList just lists every possible free move, and then you specify
    #a sub array of 1 3 7 9 for picking off the corners, if mvoe!= None means if any one of them are free take that one
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    #try to take the center (this needs to be adjusted, it's not good tictactoe strat)to
    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            #Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break