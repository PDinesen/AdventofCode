import AOCH


def position(item, ref=None):
    if ref is None:
        ref = [0, 0]
    i = 0
    while i < len(item):
        if item[i] == 'e':
            ref[1] += 1
        elif item[i] == 'w':
            ref[1] -= 1
        elif item[i] == 'n':
            ref[0] -= 1
            if item[i+1] == 'e':
                ref[1] += 0.5
            else:
                ref[1] -= 0.5
            i += 1
        else:
            ref[0] += 1
            if item[i + 1] == 'e':
                ref[1] += 0.5
            else:
                ref[1] -= 0.5
            i += 1
        i += 1

    return ref


def run(filename):
    input_list = AOCH.ril(filename)
    res_set_black = {}
    for item in input_list:
        pos = str(position(item))
        if pos in res_set_black.keys():
            res_set_black.pop(pos)
        else:
            res_set_black[pos] = 'Black'

    return res_set_black


def key_to_list(key):
    split_key = key[1:-1].split(',')
    return [int(split_key[0]), float(split_key[1])]


def adjacent(res_set_black, place):
    count = 0
    for i in [-1, 0, 1]:
        if i == 0:
            for j in [-1.0, 1.0]:
                try:
                    if res_set_black[str([place[0], place[1] + j])] == 'Black':
                        count += 1
                except KeyError:
                    continue
        else:
            for j in [-0.5, 0.5]:
                try:
                    if res_set_black[str([place[0] + i, place[1] + j])] == 'Black':
                        count += 1
                except KeyError:
                    continue
    return count


def get_min_max(res_set_black):
    temp_row = []
    temp_col = []
    for key in res_set_black:
        temp = key_to_list(key)
        temp_row.append(temp[0])
        temp_col.append(temp[1])
    if min(temp_col) % 1 != 0:
        min_col = int(min(temp_col) - 0.5)
    else:
        min_col = int(min(temp_col))
    if max(temp_col) % 1 != 0:
        max_col = int(max(temp_col) + 0.5)
    else:
        max_col = int(max(temp_col))

    return [[min(temp_row), max(temp_row)], [min_col, max_col]]


def one(res_set_black):
    min_max = get_min_max(res_set_black)
    temp = res_set_black.copy()
    for row in range(min_max[0][0] - 1, min_max[0][1] + 2):
        for col in range(min_max[1][0] - 1, min_max[1][1] + 2):
            if row % 2 == 0:
                adjust = 0
            else:
                adjust = 0.5
            try:
                if res_set_black[str([row, float(col + adjust)])] == 'Black':
                    if adjacent(res_set_black, [row, float(col + adjust)]) not in [1, 2]:
                        temp.pop(str([row, float(col + adjust)]))
            except KeyError:
                if adjacent(res_set_black, [row, float(col + adjust)]) == 2:
                    temp[str([row, float(col + adjust)])] = 'Black'

    return temp


def run2(filename, times):
    res_set_black = run(filename)
    for _ in range(times):
        res_set_black = one(res_set_black)
    return len(res_set_black)


print(run2('input24.txt', 100))
