from board_folder import can_fold_left
from board_folder import can_fold_right
from board_folder import can_fold_up
from board_folder import can_fold_down


def is_game_over(board):
    return not (can_fold_left(board) or can_fold_right(board) or can_fold_up(board) or can_fold_down(board))
