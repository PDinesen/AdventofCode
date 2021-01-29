import AOCH

input11 = AOCH.ril('input11.txt')


def adjacent(list_name, i, j):
    temp = ''
    for k in range(-1, 2):
        for l in range(-1, 2):
            if i + k in range(len(list_name)):
                if j+l in range(len(list_name[i])) and abs(k) + abs(l) != 0:
                    temp += list_name[i+k][j+l]
    return temp


def one(list_name):
    temp = []
    for i in range(len(list_name)):
        temp1 = ''
        for j in range(len(list_name[i])):
            adjacents = adjacent(list_name, i, j)
            if list_name[i][j] == 'L':
                if '#' not in adjacents:
                    temp1 += '#'
                else:
                    temp1 += 'L'
            elif list_name[i][j] == '#':
                if adjacents.count('#') >= 4:
                    temp1 += 'L'
                else:
                    temp1 += '#'
            elif list_name[i][j] == '.':
                temp1 += '.'
        temp.append(temp1)

    return temp


def run(list_name):
    last_m = list_name.copy()
    while last_m != one(last_m):
        last_m = one(last_m)

    count = 0
    for i in last_m:
        count += i.count('#')

    return count


print(run(input11))


def adjacent2(list_name, i, j):
    count = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            n = 1
            occupied = False
            while i + k*n in range(len(list_name)) \
                    and j + l*n in range(len(list_name[i])) \
                    and abs(k) + abs(l) != 0 \
                    and not occupied:
                if list_name[i+k*n][j+l*n] == '#':
                    count += 1
                    occupied = True
                elif list_name[i+k*n][j+l*n] == 'L':
                    occupied = True
                n += 1
    return count


def one2(list_name):
    temp = []
    for i in range(len(list_name)):
        temp1 = ''
        for j in range(len(list_name[i])):
            adjacents = adjacent2(list_name, i, j)
            if list_name[i][j] == 'L':
                if adjacents == 0:
                    temp1 += '#'
                else:
                    temp1 += 'L'
            elif list_name[i][j] == '#':
                if adjacents >= 5:
                    temp1 += 'L'
                else:
                    temp1 += '#'
            elif list_name[i][j] == '.':
                temp1 += '.'
        temp.append(temp1)

    return temp


def run2(list_name):
    last_m = list_name.copy()
    while last_m != one2(last_m):
        last_m = one2(last_m)

    count = 0
    for i in last_m:
        count += i.count('#')

    return count


print(run2(input11))
