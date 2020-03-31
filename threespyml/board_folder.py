from line_folder import fold
from line_folder import can_fold
from board_rotator import rotate
import copy

def fold_left(state):
    return list(map(fold, state))


def fold_up(state):
    state = rotate(state, 3)
    state = list(map(fold, state))
    return rotate(state, 1)


def fold_down(state):
    state = rotate(state, 1)
    state = list(map(fold, state))
    return rotate(state, 3)


def fold_right(state):
    state = rotate(state, 2)
    state = list(map(fold, state))
    return rotate(state, 2)


def can_fold_left(board):
    return any(list(map(can_fold, board)))


def can_fold_right(board):
    state = copy.deepcopy(board)
    state = rotate(state, 2)
    return any(list(map(can_fold, state)))


def can_fold_down(board):
    state = copy.deepcopy(board)
    state = rotate(state, 1)
    return any(list(map(can_fold, state)))


def can_fold_up(board):
    state = copy.deepcopy(board)
    state = rotate(state, 3)
    return any(list(map(can_fold, state)))

