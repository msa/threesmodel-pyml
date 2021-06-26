

def translate_left_fold(candidates):
    return candidates


def translate(candidates, translator):
    result = []
    for candidate in candidates:
        result.append(translator[candidate[0]])
    return result


def translate_right_fold(candidates):
    return translate(candidates, {3: [0, 0], 2: [1, 0], 1: [2, 0], 0: [3, 0]})


def translate_down_fold(candidates):
    return translate(candidates, {3: [0, 3], 2: [0, 2], 1: [0, 1], 0: [0, 0]})


def translate_up_fold(candidates):
    return translate(candidates, {3: [3, 0], 2: [3, 1], 1: [3, 2], 0: [3, 3]})
