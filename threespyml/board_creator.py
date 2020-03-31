import random


def create_game_board():
    positions = random_positions(9)
    return assemble_game_board(positions)


def assemble_game_board(positions):
    rows = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for position in positions:
        rows[position[0]][position[1]] = random.randrange(1, 4)
    return rows


def random_positions(number_of_positions):
    positions = []
    while len(positions) < number_of_positions:
        candidate_position = [random.randrange(0, 4), random.randrange(0, 4)]
        if candidate_position not in positions:
            positions.append(candidate_position)
    return positions
