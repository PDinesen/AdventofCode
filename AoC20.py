import AOCH
from math import sqrt
import copy


def initialize(filename):
    input_list = AOCH.ril2(filename, '')
    input_set = {}
    for item in input_list:
        input_set[item[0].split(' ')[1][:-1]] = item[1:]
    return input_set


def rotate(list_input):
    temp = []
    for i in reversed(range(len(list_input))):
        text = ''
        for j in range(len(list_input)):
            text += list_input[j][i]
        temp.append(text)
    return temp


def get_link(input_set):
    temp_set = {}
    for key1 in input_set:
        temp1 = ['']*4
        for j in range(4):
            for key2 in input_set:
                if key1 != key2:
                    for _ in range(4):
                        for _ in range(2):
                            if input_set[key1][0] == input_set[key2][-1]:
                                temp1[j] = key2
                            input_set[key2] = input_set[key2][::-1]
                        input_set[key2] = rotate(input_set[key2])
            input_set[key1] = rotate(input_set[key1])
        temp_set[key1] = temp1
    return temp_set


def run(filename):
    input_set = initialize(filename)
    temp = get_link(input_set)
    prod = 1
    for key in temp:
        if temp[key].count('') == 2:
            prod *= int(key)
    print(prod)

# run('input20.txt')


def is_good(check, against, side):
    if side == 'R':
        if [check[i][-1] for i in range(len(check))] == [against[i][0] for i in range(len(against))]:
            return True
        else:
            return False
    if side == 'D':
        if check[-1] == against[0]:
            return True
        else:
            return False


def flip_sideways(list_input):
    for i in range(len(list_input)):
        list_input[i] = list_input[i][::-1]
    return list_input


def print_tables(input_list):
    for i in range(len(input_list)):
        for j in range(len(input_list[i][0])):
            print_text = ''
            for k in range(len(input_list[i])):
                print_text += input_list[i][k][j] + ' '
            print(print_text)
        print(' ')


def connect_image(filename):
    input_set = initialize(filename)
    linked = get_link(input_set)
    length = int(sqrt(len(input_set)))
    temp = []
    for _ in range(length):
        temp.append(['']*length)
    temp4 = []
    for _ in range(length):
        temp4.append([''] * length)
    print(linked)
    for key in linked:
        if linked[key][2] + linked[key][3] == '':
            start_key = key
            break
    temp[0][0] = start_key
    temp[0][1] = linked[start_key][1]
    temp[1][0] = linked[start_key][0]
    print(linked[start_key])
    temp1, temp2, temp3 = (0,0,0)
    for _ in range(4):
        for _ in range(4):
            for _ in range(2):
                if is_good(input_set[start_key], input_set[linked[start_key][0]], 'D'):
                    temp1 = input_set[start_key]
                    temp2 = input_set[linked[start_key][0]]
                    for _ in range(2):
                        for _ in range(4):
                            for _ in range(2):
                                if is_good(temp1, input_set[linked[start_key][1]], 'R'):
                                    temp3 = input_set[linked[start_key][1]]
                                input_set[linked[start_key][1]] = input_set[linked[start_key][1]][::-1]
                            input_set[linked[start_key][1]] = rotate(input_set[linked[start_key][1]])
                        if temp3 == 0:
                            temp1 = flip_sideways(temp1)
                            temp2 = flip_sideways(temp2)
                input_set[linked[start_key][0]] = input_set[linked[start_key][0]][::-1]
            input_set[linked[start_key][0]] = rotate(input_set[linked[start_key][0]])
        input_set[start_key] = rotate(input_set[start_key])
    used = [start_key, linked[start_key][0], linked[start_key][1]]
    print(used, temp)
    temp4[0][0] = temp1
    temp4[0][1] = temp3
    temp4[1][0] = temp2
    print(temp4)

    for i in range(length):
        for j in range(length):
            for key in input_set:
                if key not in used:
                    for _ in range(4):
                        for _ in range(2):
                            if is_good(temp4[i][j], input_set[key], 'R'):
                                temp4[i][j+1] = copy.deepcopy(input_set[key])
                                used.append(key)
                                temp[i][j+1] = key
                            elif is_good(temp4[i][j], input_set[key], 'D'):
                                temp4[i + 1][j] = copy.deepcopy(input_set[key])
                                used.append(key)
                                temp[i + 1][j] = key
                            input_set[key] = flip_sideways(input_set[key])
                        input_set[key] = rotate(input_set[key])
    print(temp)
    print_tables(temp4)
    return temp4


def remove_gabs(input_list):
    temp = []
    for i in range(len(input_list)):
        for j in range(1, len(input_list[i][0])-1):
            print_text = ''
            for k in range(len(input_list[i])):
                print_text += input_list[i][k][j][1:-1]
            temp.append(print_text)
    return temp

def change_string_item(string_input, col, elem):
    if col == 0:
        return elem + string_input[1:]
    elif col == len(string_input):
        return string_input[:-1] + elem
    else:
        return string_input[:col] + elem + string_input[col+1:]



def run2(filename):
    input_list = connect_image(filename)
    image = remove_gabs(input_list)
    for _ in range(4):
        for _ in range(2):
            for i in range(1, len(image)-1):
                for j in range(len(image[i])-19):
                    if image[i][j] == '#' and image[i+1][j+1] == '#'\
                            and image[i+1][j+4] == '#' and image[i][j+5] == '#' and image[i][j+6] == '#' and image[i+1][j+7] == '#'\
                            and image[i+1][j+10] == '#' and image[i][j+11] == '#' and image[i][j+12] == '#' and image[i+1][j+13] == '#'\
                            and image[i+1][j+16] == '#' and image[i][j+17] == '#' and image[i][j+18] == '#' and image[i-1][j+18] == '#' and image[i][j+19] == '#':
                        image[i] = change_string_item(image[i], j, 'O')
                        image[i + 1] = change_string_item(image[i+1], j+1, 'O')
                        image[i + 1]= change_string_item(image[i+1], j+4, 'O')
                        image[i] = change_string_item(image[i], j+5, 'O')
                        image[i] = change_string_item(image[i], j+6, 'O')
                        image[i + 1] = change_string_item(image[i+1], j+7, 'O')
                        image[i + 1] = change_string_item(image[i+1], j+10, 'O')
                        image[i] = change_string_item(image[i], j+11, 'O')
                        image[i] = change_string_item(image[i], j+12, 'O')
                        image[i + 1] = change_string_item(image[i+1], j+13, 'O')
                        image[i + 1] = change_string_item(image[i+1], j+16, 'O')
                        image[i] = change_string_item(image[i], j+17, 'O')
                        image[i] = change_string_item(image[i], j+18, 'O')
                        image[i - 1] = change_string_item(image[i-1], j+18, 'O')
                        image[i] = change_string_item(image[i], j+19, 'O')
                        temp = copy.deepcopy(image)
            image = image[::-1]
        image = rotate(image)
    count = 0
    for item in temp:
        count += item.count('#')
        print(item)
    print(count)




run2('input20.txt')



# connect_image('test')
# connect_image('input20.txt')
# test = '123'
# print(test[1:-1])




