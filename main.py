import numpy as np
import math
human=0
algorithm=1
hpiece=1
algopiece=2
def creatingboard():
    board=np.zeros((6,7))#shape of board
    return board
def drop(board,row,col,piece):
    board[row][col]=piece
def validation(board,col):
    return board[5][col]==0#[row][col]check the col is fil or no #check last index of the rows in the column
def getvalidlocations(board):
    validlocations=[]
    for c in range(7):
        if validation(board,c):
            validlocations.append(c)
    return validlocations
def get_next(board,col):
    for r in range (6):
        if board[r][col]==0:#if the columns is not fill up choose the row
            return r
def final_board(board):
    print(np.flip(board,0))#star at end
def win(board,piece):

    # check horizntal
    for c in range (4):#COLUMNS-3
        for r in range(6):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True

    #check vertical
    for c in range (7):
        for r in range(3):#ROW-3
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True

    # check positvily diagonal
    for c in range (4):#COLUMNS-3
        for r in range(3):#ROW-3
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True

    # check negativly diagonal
    for c in range (4):#COLUMNS-3
        for r in range(3,6):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True
def evaluate_window(window, piece):
    score = 0
    opp_piece = 1
    if piece == 1:
        opp_piece = 2

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 10
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 5
    if window.count(opp_piece) == 3 and window.count(0) == 1:
        score -= 100
    return score
def score_position(board, piece):
    score = 0

    ## Score center column
    center_array = [int(i) for i in list(board[:, 4])]
    center_count = center_array.count(piece)
    score += center_count * 6

    # Score Horizontal
    for r in range(6):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(4):#COL - 3
            window = row_array[c:c + 4]
            score += evaluate_window(window, piece)

    # Score Vertical
    for c in range(7):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(3):#ROW- 3
            window = col_array[r:r + 4]
            score += evaluate_window(window, piece)

    # Score positive diagonal
    for r in range(3):#ROW - 3
        for c in range(4):#COLUMN- 3
            window = [board[r + i][c + i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Score negativly diagonal
    for r in range(3):#ROW - 3
        for c in range(4):#COLUMN3
            window = [board[r + 3 - i][c + i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score
def is_terminal_node(board):
    return win(board, 1) or win(board, 2) or len(getvalidlocations(board)) == 0
def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = getvalidlocations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if win(board, 1):
                return (None, -100000000000000)
            elif win(board, 2):
                return (None, 10000000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, score_position(board, 2))
    if maximizingPlayer:
        value = -math.inf
        column = valid_locations[0]

        for col in valid_locations:
            row = get_next(board, col)
            b_copy = board.copy()
            drop(b_copy, row, col, 2)
            new_score = minimax(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value


    else:
        value = math.inf
        column = valid_locations[0]
        for col in valid_locations:
            row = get_next(board, col)
            b_copy = board.copy()
            drop(b_copy, row, col, 1)
            new_score = minimax(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

game_over=False
board=creatingboard()
final_board(board)
turn=0

while not game_over:
    if turn ==human:
        col=int(input("The first player 1 choice is: "))#(0:6)
        if validation(board,col):
            row=get_next(board,col)
            drop(board,row,col,1)
            if win(board,1):
                print("***** player won ******")
                game_over=True

    if turn ==algorithm:
        col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)
        if validation(board,col):
            row=get_next(board,col)
            drop(board,row,col,2)
            if win(board,2):
                print("***** player lost ******")
                game_over=True
    turn+=1
    turn=turn%2 #0or1
    final_board(board)