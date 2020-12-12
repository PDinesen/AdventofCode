import AOCH

input6 = AOCH.ril('input6.txt')
print(input6)


def run(input_list):
    count = 0
    temp = []

    for i in input_list:
        if i == '':
            count += len(temp)
            temp = []
        else:
            for j in i:
                if j not in temp:
                    temp.append(j)
    count += len(temp)
    return count


print('Part 1: ' + str(run(input6)))


def run2(input_list):
    count = 0
    for i in input_list:
        temp = []
        for j in range(len(i)):
            for k in i[j]:
                in_all = True
                for l in range(len(i)):
                    if k not in i[l] or k in temp:
                        in_all = False
                        continue
                if in_all:
                    temp.append(k)
        count += len(temp)
    return count


print('Part 2: ' + str(run2(AOCH.group(input6, ''))))
