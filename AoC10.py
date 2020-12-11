import AOCH

input10 = AOCH.ril('input10.txt')

input10 = list(map(int, input10))
input10.append(0)
input10.append(max(input10) + 3)
input10 = sorted(input10)


def diff_in_list(input_list):
    temp = []
    for i in range(1, len(input_list)):
        temp.append(input_list[i] - input_list[i - 1])
    return temp


def run(input_list):
    temp = diff_in_list(input_list)

    return [temp.count(1), temp.count(3), temp.count(1) * temp.count(3)]


print(run(input10)[2])


def rec_pas(value):
    if value == 0 or value == 1:
        return 1
    elif value == 2:
        return 2
    elif value == 3:
        return 4
    else:
        return rec_pas(value - 1) + rec_pas(value - 2) + rec_pas(value - 3)


def run2(input_list):
    temp = diff_in_list(input_list)
    count = 0
    res = 1
    for i in range(len(temp)):
        if temp[i] == 3:
            res *= rec_pas(count)
            count = 0
        else:
            count += 1
    return res


print(run2(input10))
