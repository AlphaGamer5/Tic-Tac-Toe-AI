"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board is initial_state():
        return X

    countX = 0
    countO = 0

    for row in board:
        countX += row.count(X)
        countO += row.count(O)
    
    if countX > countO:
        return O
    else:
        return X
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                actions.add((row,col))
    return actions
            
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] not in range(3) or action[1] not in range(3) or board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)

    return new_board

    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for mark in [X,O]:
        for row in range(0,3):
            if all(board[row][col] == mark for col in range(0,3)):
                return mark
        
        for col in range(0,3):
            if all(board[row][col] == mark for row in range(0,3)):
                return mark
        
        diagonals = [[(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
        for diag in diagonals:
            if all(board[r][c] == mark for (r,c) in diag):
                return mark

    return None
    
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    all_moves = [cell for row in board for cell in row]
    if not any(move==EMPTY for move in all_moves):
        return True

    return False
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) ==  X:
        return 1
    if winner(board) == O:
        return -1
    return 0
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    bestAction = None
    if terminal(board):
        return None

    if player(board) == X:
        value = -math.inf
        for action in actions(board):
            maxValue = minimizer(result(board,action))
            if maxValue > value:
                value = maxValue
                bestAction = action
    elif player(board) == O:
        value = math.inf
        for action in actions(board):
            minValue = maximizer(result(board,action))
            if minValue < value:
                value = minValue
                bestAction = action
    return bestAction
    # raise NotImplementedError

def minimizer(board):
    if terminal(board):
        return utility(board)

    value = math.inf
    for action in actions(board):
        value = min(value,maximizer(result(board,action)))
    
    return value

def maximizer(board):
    if terminal(board):
        return utility(board)

    value = -math.inf
    for action in actions(board):
        value = max(value,minimizer(result(board,action)))

    return value

