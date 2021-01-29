import AOCH
import copy

def append_row_and_col(input_list):
    temp = ['.']*(len(input_list)+2)
    res = [temp]
    for i in input_list:
        res.append(['.'] + i + ['.'])
    res.append(temp)
    return res


def append_dimension(input_list):
    temp = [['.']*len(input_list[0][0]) for _ in range(len(input_list[0]))]
    return [temp] + input_list + [temp]


def initialize(filename, cycles):
    first_state = AOCH.ril(filename)
    for i in range(len(first_state)):
        temp1 = []
        for j in range(len(first_state[i])):
            temp1.append(first_state[i][j])
        first_state[i] = temp1
    for _ in range(cycles):
        first_state = append_row_and_col(first_state)
    res = [first_state]
    for _ in range(cycles):
        res = append_dimension(res)

    return res


def count_neighbors(list_name, dim, row, col):
    count = 0
    for x in range(-1, 2):
        if x + dim in range(len(list_name)):
            for y in range(-1, 2):
                if y + row in range(len(list_name[x])):
                    for z in range(-1, 2):
                        if z + col in range(len(list_name[x][y])) and abs(x) + abs(y) + abs(z) != 0:
                            if list_name[x + dim][y + row][z + col] == '#':
                                count += 1
    return count


def count_element(input_list, element):
    count = 0
    for dim in input_list:
        for row in dim:
            for col in row:
                if col == element:
                    count += 1
    return count


def one(input_list):
    temp = copy.deepcopy(input_list)
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            for k in range(len(input_list[i][j])):
                if input_list[i][j][k] == '#':
                    if count_neighbors(input_list, i, j, k) not in [2, 3]:
                        temp[i][j][k] = '.'
                else:
                    if count_neighbors(input_list, i, j, k) == 3:
                        temp[i][j][k] = '#'
    return temp


def print_table(input_list):
    for i in input_list:
        print(i)


def run(filename, cycles):
    input_list = initialize(filename, cycles)
    for _ in range(cycles):
        input_list = one(input_list)
        # print(count_element(input_list, '#'))
    return input_list


def append_dimension2(input_list):
    temp = [[['.']*len(input_list[0][0][0]) for _ in range(len(input_list[0][0]))] for _ in range(len(input_list[0]))]
    return [temp] + input_list + [temp]


def initialize2(filename, cycles):
    first_state = AOCH.ril(filename)
    for i in range(len(first_state)):
        temp1 = []
        for j in range(len(first_state[i])):
            temp1.append(first_state[i][j])
        first_state[i] = temp1
    for _ in range(cycles):
        first_state = append_row_and_col(first_state)
    res = [first_state]
    for _ in range(cycles):
        res = append_dimension(res)
    res = [res]
    for _ in range(cycles):
        res = append_dimension2(res)
    return res


def count_neighbors2(list_name, dim2, dim, row, col):
    count = 0
    for v in range(-1, 2):
        if v + dim2 in range(len(list_name)):
            for x in range(-1, 2):
                if x + dim in range(len(list_name[0])):
                    for y in range(-1, 2):
                        if y + row in range(len(list_name[0][0])):
                            for z in range(-1, 2):
                                if z + col in range(len(list_name[0][0][0])) and abs(v) + abs(x) + abs(y) + abs(z) != 0:
                                    if list_name[v + dim2][x + dim][y + row][z + col] == '#':
                                        count += 1
    return count


def count_element2(input_list, element):
    count = 0
    for dim2 in input_list:
        for dim in dim2:
            for row in dim:
                for col in row:
                    if col == element:
                        count += 1
    return count


def one2(input_list):
    temp = copy.deepcopy(input_list)

    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            for k in range(len(input_list[i][j])):
                for l in range(len(input_list[i][j][k])):
                    if input_list[i][j][k][l] == '#':
                        if count_neighbors2(input_list, i, j, k, l) not in [2, 3]:
                            temp[i][j][k][l] = '.'
                    else:
                        if count_neighbors2(input_list, i, j, k, l) == 3:
                            temp[i][j][k][l] = '#'
    return temp


def run2(filename, cycles):
    input_list = initialize2(filename, cycles)
    for _ in range(cycles):
        input_list = one2(input_list)
        print(count_element2(input_list, '#'))
    return input_list


for i in range(7):
    print('---------%d-----------' %i)
    test = run('test1', i)
    for j in range(len(test)):
        print('---------%d-------' %(j - i))
        print_table(test[j])
