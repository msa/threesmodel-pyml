score_table = {0: 0, 1: 0, 2: 0,
               3: 3,
               6: 9,
               12: 27,
               24: 81,
               48: 243,
               96: 729,
               192: 2187,
               384: 6561,
               768: 19683,
               1536: 59049,
               3072: 177147,
               6144: 531441,
               12288: 1594323,
               24576: 4782969}

def score_for(board):
    return sum(list(map(sum, list(map(score_for_line, board)))))


def score_for_line(line):
    return list(map(score_for_cell, line))


def score_for_cell(cell_value):
    return score_table[cell_value]
