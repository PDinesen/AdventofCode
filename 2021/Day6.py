ind = [list(map(int, line.split(','))) for line in open('input6.txt')][0]


def initial(input_list):
    dict_fish = {}
    for i in range(9):
        dict_fish[i] = sum(j == i for j in input_list)
    return dict_fish


def one_day2(dictionary):
    zeros = dictionary[0]
    for key in range(1, 9):
        fish = dictionary[key]
        dictionary[key - 1] = fish
    dictionary[6] += zeros
    dictionary[8] = zeros
    return dictionary


def run(n, input_list):
    dictionary = initial(input_list)
    temp = dictionary.copy()
    for _ in range(n):
        temp = one_day2(temp)
    print(sum(i for i in temp.values()))


run(80, ind)
run(256, ind)
