import AOCH
from operator import itemgetter


def initialize(filename):
    input_list = AOCH.ril(filename)
    temp = []
    for i in range(len(input_list)):
        input_list[i] = input_list[i].split(' (')
        input_list[i][0] = input_list[i][0].split(' ')
        input_list[i][1] = input_list[i][1][9:-1].split(', ')
        for item in input_list[i][1]:
            if item not in temp:
                temp.append(item)
    return input_list, temp


print(initialize('test'))


def run(filename):
    input_list, allergens = initialize(filename)
    temp_set = {}
    for item in allergens:
        temp = []
        for food in input_list:
            if item in food[1]:
                if len(temp) == 0:
                    temp = food[0]
                else:
                    temp = [ingred for ingred in temp if ingred in food[0]]
        temp_set[item] = temp
    res = []
    while len(temp_set) > 0:
        print(temp_set)
        for key in temp_set:
            if len(temp_set[key]) == 1:
                item = temp_set[key][0]
                remove = key
                break
        temp_set.pop(remove)
        for i in range(len(input_list)):
            if item in input_list[i][0]:
                input_list[i][0].remove(item)
        print(input_list)
        for key1 in temp_set:
            if item in temp_set[key1]:
                temp_set[key1].remove(item)
        res.append([remove, item])
    count = sum([len(item[0]) for item in input_list])
    print(count)
    result_string = ''
    for item in sorted(res, key=itemgetter(0)):
        result_string += item[1] + ','
    print(result_string[:-1])

    print(temp_set)

    return 0

run('input21.txt')

