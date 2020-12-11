from operator import itemgetter


def ril(filename):
    return [line.rstrip('\n') for line in open(filename)]


def ril2(filename, split_item):
    temp = [line.rstrip('\n') for line in open(filename)]
    return group(temp, split_item)


def ricl(filename):
    lines = ril(filename)
    return lines[0].split(',')


def split_by(list_name: list, character):
    temp = []
    for i in list_name:
        temp.append(i.split(character))
    return temp


def risl(line):
    return line.split(' ')


def group(list_name, split):
    temp = []
    res = []
    for i in list_name:
        if i == split:
            res.append(temp)
            temp = []
        else:
            temp.append(i)
    res.append(temp)
    return res


def stt(list_name):
    temp = []
    for i in list_name:
        temp.append(int(i))
    return temp


def password_input(filename):
    input2 = ril(filename)

    for i in range(len(input2)):
        input2[i] = risl(input2[i])
        temp = input2[i][0].split('-')
        input2[i][0] = [int(temp[0]), int(temp[1])]
    return input2


def passport(filename):
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
