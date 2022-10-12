from time import sleep
from random import choice

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    return '''
    +--------+--------+--------+
    |        |        |        |
    |   {}    |   {}    |   {}    |
    |        |        |        |
    +--------+--------+--------+
    |        |        |        |
    |   {}    |   {}    |   {}    |
    |        |        |        |
    +--------+--------+--------+
    |        |        |        |
    |   {}    |   {}    |   {}    |
    |        |        |        |
    +--------+--------+--------+
    '''.format(board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2],board[2][0],board[2][1],board[2][2])


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    valid = []
    for x in range(len(board)):
        for y in board[x]:
            if y != 'x' and y != 'o':
                valid.append(y)
                
    print('valid moves ', valid)
    try:
        p_move = int(input('Enter your move: '))
        for x in range(len(board)):
            for y in board[x]:
                if (p_move in valid) and (y == p_move):
                    row = x
                    col = board[x].index(y)
        board[row][col] = 'o'
        print(display_board(board))
        return True
    except:
        print('Invalid Entry, ', p_move,' Miss a turn')
        sleep(3)
        print(display_board(board))
        return False
        
        
        
def com_move(board):
    valid = []
    for x in range(len(board)):
        for y in board[x]:
            if y != 'x' and y != 'o':
                valid.append(y)
    	    
    print('valid moves ', valid)
    c_move = choice(valid)
    print('Computer moves: ',c_move)
    sleep(2)
    try:
        for x in range(len(board)):
            for y in board[x]:
                if (c_move in valid) and (y == c_move):
                    row = x
                    col = board[x].index(y)
        board[row][col] = 'x'
        print(display_board(board))
        return True
    except:
        print('Invalid Entry, ', c_move,' Miss a turn')
        sleep(3)
        print(display_board(board))
        return True


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    #valid = []
    valid_t = []
    for x in range(len(board)):
        for y in board[x]:
            if y != 'x' and y != 'o':
                #valid.append(y)
                row = x
                col = board[x].index(y)
                valid_t.append((row,col))
    return valid_t


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if len(make_list_of_free_fields(board)) > 6:
        return False
    if sign == "o":
        if board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o': return True
        if board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o': return True
        if board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o': return True
        if board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o': return True
        if board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o': return True
        if board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o': return True
        if board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o': return True
        if board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o': return True
        
    if sign == "x":
        if board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x': return True
        if board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x': return True
        if board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x': return True
        if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x': return True
        if board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x': return True
        if board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x': return True
        if board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x': return True
        if board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x': return True
        
    return False   
    

def draw_move(board):
    # The function draws the computer's move and updates the board.
    if len(make_list_of_free_fields(board)) == 0:
        return True
    else: return False

def play_ttt():
    board = [[1,2,3],[4,5,6],[7,8,9]]
    status = True
    print(display_board(board))
    while status == True:
        user = enter_move(board)
        if user == True:
            u_vic = victory_for(board, 'o')
            if u_vic == True:
                print('You Won')
                status = False
                continue
        draw = draw_move(board)
        if draw == True:
            print('The game ended in a draw')
            status = False
            continue
        com = com_move(board)
        if com == True:
            c_vic = victory_for(board, 'x')
            if c_vic == True:
                print('Computer Won')
                status = False
                continue
        draw = draw_move(board)
        if draw == True:
            print('The game ended in a draw')
            status = False
            continue


play_ttt()