from operator import itemgetter


def ril(filename):
    return [line.rstrip('\n') for line in open(filename)]


def split_by(list_name: list, character):
    temp = []
    for i in list_name:
        temp.append(i.split(character))
    return temp


def make_set(input_list):
    temp2 = {}
    for i in input_list:
        temp3 = []
        for j in range(3, len(i)):
            if i[j][:3] == 'bag' or i[j] == 'bags':
                temp3.append([i[j - 3], i[j - 2] + ' ' + i[j - 1]])
        temp2[i[0] + ' ' + i[1]] = temp3
    return temp2


def day1(filename):
    return list(map(int, ril(filename)))


def day2(filename):
    input2 = ril(filename)

    for i in range(len(input2)):
        input2[i] = input2[i].split(' ')
        input2[i][1] = input2[i][1][:-1]
        temp = input2[i][0].split('-')
        input2[i][0] = [int(temp[0]), int(temp[1])]
    return input2


def day3(filename):
    return ril(filename)


def day4(filename):
    input4 = ril(filename)
    temp6 = []
    temp7 = []
    for i in input4:
        if i == '':
            temp6.append(sorted(temp7, key=itemgetter(0)))
            temp7 = []
        else:
            for line in i.split(' '):
                temp7.append(line.split(':'))
    if len(temp7) != 0:
        temp6.append(sorted(temp7, key=itemgetter(0)))

    return temp6


def day5(filename):
    return ril(filename)


def day6(filename):
    temp = []
    temp2 = []

    for i in ril(filename):
        if i == '':
            temp.append(temp2)
            temp2 = []
        else:
            temp2.append(i)
    temp.append(temp2)
    return temp


def day7(filename):
    return make_set(split_by(ril(filename), ' '))


def day8(filename):
    input8 = ril(filename)

    temp = []
    for i in range(len(input8)):
        temp.append(input8[i].split(' '))
        temp[i][1] = int(temp[i][1])
    return temp


def day9(filename):
    return list(map(int, ril(filename)))


def day10(filename):
    temp = list(map(int, ril(filename)))
    temp.append(0)
    temp.append(max(temp) + 3)
    return sorted(temp)


def day11(filename):
    return ril(filename)


def day12(filename):
    return ril(filename)
