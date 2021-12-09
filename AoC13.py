import AOCH
from math import lcm


def initialize(filename):
    input13 = AOCH.ril(filename)
    input13[0] = int(input13[0])
    input13[1] = input13[1].split(',')
    temp = []
    for j in input13[1]:
        if j != 'x':
            temp.append(int(j))
    return [input13[0], temp]


def run(filename):
    input_list = initialize(filename)
    my_time = input_list[0]
    best_wait = my_time
    best_id = input_list[1][0]
    for value in input_list[1]:
        if -my_time % value < best_wait:
            best_id = value
            best_wait = -my_time % value

    return [best_wait, best_id, best_wait * best_id]


print(run('input13-1.txt'))


def find_step(first, second):
    i = first
    while True:
        if i % second == 0:
            return i
        i += first


def find_n(step, n, second, between):
    i = n
    while True:
        if (i + between) % second == 0:
            return i
        i += step


def run2(filename):
    input_list = AOCH.ril(filename)[1].split(',')
    print(input_list)
    between = []
    ids = []
    for i in range(len(input_list)):
        if input_list[i] != 'x':
            between.append(i)
            ids.append(int(input_list[i]))
    step = ids[0]
    n = 0
    for i in range(1, len(between)):
        print('n = ' + str(n) + ' og step = ' + str(step))
        n = find_n(step, n, ids[i], between[i])
        step = lcm(step, ids[i])
    return n


print(initialize('input13-1.txt'))
print(run2('input13-1.txt'))
