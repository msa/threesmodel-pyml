import random

def highest_number(game_board):
    flat_board = flatten(game_board)
    return max(flat_board)


def select_number(game_board):
    possible_cells = [0, 1, 2, 3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144]
    index = random.randrange(1, (max([3, possible_cells.index(highest_number(game_board)) - 2])))

    return possible_cells[index]


def flatten(game_board):
    flat_list = []
    for row in game_board:
        for cell in row:
            flat_list.append(cell)
    return flat_list