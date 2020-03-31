def rotate(board, times):
    if times == 0:
        return board
    else:
        return rotate(one_rotation(board), times - 1)


def one_rotation(board):
    return [[board[3][0], board[2][0], board[1][0], board[0][0]],
            [board[3][1], board[2][1], board[1][1], board[0][1]],
            [board[3][2], board[2][2], board[1][2], board[0][2]],
            [board[3][3], board[2][3], board[1][3], board[0][3]]]
