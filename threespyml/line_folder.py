def wall_index_of(line):
    if (line == ([1, 1, 1, 1] or [2, 2, 2, 2])):
        return 3
    if line[1:4] == [0, 0, 0]:
        return 3
    if line[0] == 0:
        return 0
    if line[0] == 1 and line[1] == 2:
        return 0
    if line[0] == 2 and line[1] == 1:
        return 0
    if line[0] > 2:
        if line[0] == line[1]:
            return 0

    if line[2:4] == [0, 0]:
        return 3
    if line[1] == 0:
        return 1
    if (line[0] != line[1]) and line[1] == 1 and line[2] == 2:
        return 1
    if (line[0] != line[1]) and line[1] == 2 and line[2] == 1:
        return 1
    if (line[0] == line[1]) and line[1] == 1 and line[2] == 2:
        return 1
    if (line[0] == line[1]) and line[1] == 2 and line[2] == 1:
        return 1
    if line[1] > 2:
        if line[1] == line[2]:
            return 1
    if line[2] == 0:
        return 2
    if line[2] == 1 and line[3] == 2:
        return 2
    if line[2] == 2 and line[3] == 1:
        return 2
    if line[2] > 2:
        if line[2] == line[3]:
            return 2
    return 3

def fold(line):
    if (can_fold(line)):
        folded_line = line.copy()
        wall_index = wall_index_of(folded_line)
        folded_line[wall_index] = folded_line[wall_index] + folded_line[wall_index + 1]
        while wall_index < 2:
            folded_line[wall_index + 1] = folded_line[wall_index + 2]
            wall_index += 1
        folded_line[3] = 0
        return folded_line
    return line

def can_fold(line):
    return wall_index_of(line) < 3
