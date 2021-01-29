import AOCH


def splitting(filename):
    input16 = AOCH.ril2(filename, '')
    for i in range(len(input16[0])):
        input16[0][i] = input16[0][i].split(': ')
        input16[0][i][1] = input16[0][i][1].split(' or ')
        for j in range(len(input16[0][i][1])):
            input16[0][i][1][j] = list(map(int, input16[0][i][1][j].split('-')))
    input16[1][1] = list(map(int, input16[1][1].split(',')))

    for i in range(1, len(input16[2])):
        input16[2][i] = list(map(int, input16[2][i].split(',')))
    return input16


input16 = splitting('input16.txt')


def check_valid(list_name, number):
    for i in range(len(list_name[0])):
        for j in range(len(list_name[0][i][1])):
            if number in range(list_name[0][i][1][j][0], list_name[0][i][1][j][1] + 1):
                return True
    return False


def run(list_name):
    sum_invalid = 0
    for i in range(1, len(list_name[2])):
        for j in list_name[2][i]:
            if not check_valid(list_name, j):
                sum_invalid += j

    return sum_invalid


def in_range(list_range, number):
    for item in list_range:
        if number in range(item[0], item[1] + 1):
            return True
    return False


def remove_item(index, item):
    for i in range(len(index)):
        if item in index[i]:
            index[i].remove(item)
    return index


def run2(list_name):
    temp = []
    for i in range(1, len(list_name[2])):
        good = True
        for j in list_name[2][i]:
            if not check_valid(list_name, j):
                good = False
        if good:
            temp.append(list_name[2][i])
    index = []
    for i in range(len(temp[0])):
        index_list = []
        for item1 in list_name[0]:
            in_r = True
            for item in temp:
                if not in_range(item1[1], item[i]):
                    in_r = False
            if in_r:
                index_list.append(item1[0])
        index.append(index_list)

    res_list = {}
    for _ in range(len(index)):
        for i in range(len(index)):
            if len(index[i]) == 1:
                res_list[index[i][0]] = i
                index = remove_item(index, index[i][0])
                break
    prod = 1
    for item in res_list:
        if 'departure' in item:
            prod *= list_name[1][1][res_list[item]]
    return prod

print(run(input16))
print(run2(input16))

