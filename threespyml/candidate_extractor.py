from line_folder import can_fold
from board_rotator import rotate


def add_candidate(candidates, index, param):
    if can_fold(param):
        candidates.append([index, 3])


def fold_left_candidates(game):
    candidates = []
    for index in range(len(game)):
        add_candidate(candidates, index, game[index])

    return candidates


def fold_up_candidates(game):
    candidates = []
    rotated_board = rotate(game, 1)
    for index in range(len(rotated_board)):
        add_candidate(candidates, index, game[index])
    return candidates

def fold_down_candidates(game):
    candidates = []
    rotated_board = rotate(game, 3)
    for index in range(len(rotated_board)):
        add_candidate(candidates, index, game[index])
    return candidates


def fold_right_candidates(game):
    candidates = []
    rotated_board = rotate(game, 2)
    for index in range(len(rotated_board)):
        add_candidate(candidates, index, game[index])
    return candidates
