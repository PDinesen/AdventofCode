from copy import deepcopy
from time import time
st = [contents.rstrip('\n') for contents in open('input/' + 'day14' + '.txt')]


def change(lst, row, col, typ):
    lst[row] = lst[row][:col] + typ + lst[row][col+1:]
    return lst


def move_rock(lst, way):
    if way == 'W':
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                if lst[i][j] == 'O':
                    k = j
                    while lst[i][k-1] == '.' and k - 1 >= 0:
                        lst = change(lst, i, k, '.')
                        lst = change(lst, i, k - 1, 'O')
                        k -= 1
    elif way == 'N':
        for i in range(1, len(lst)):
            for j in range(len(lst[0])):
                if lst[i][j] == 'O':
                    k = i
                    while lst[k - 1][j] == '.' and k - 1 >= 0:
                        lst = change(lst, k, j, '.')
                        lst = change(lst, k - 1, j, 'O')
                        k -= 1
    elif way == 'E':
        for i in range(len(lst)):
            for j in range(len(lst[0]) - 1, -1, -1):
                if lst[i][j] == 'O':
                    k = j
                    while k + 1 < len(lst[0]) and lst[i][k + 1] == '.':
                        lst = change(lst, i, k, '.')
                        lst = change(lst, i, k + 1, 'O')
                        k += 1
    elif way == 'S':
        for i in range(len(lst) - 1, -1, -1):
            for j in range(len(lst[0])):
                if lst[i][j] == 'O':
                    k = i
                    while k + 1 < len(lst) and lst[k + 1][j] == '.':
                        lst = change(lst, k, j, '.')
                        lst = change(lst, k + 1, j, 'O')
                        k += 1

    return lst


def cal(lst):
    res = 0
    for row in range(len(lst)):
        for col in range(len(st[0])):
            if lst[row][col] == 'O':
                res += len(lst) - row
    return res


moved = move_rock(st, 'N')

print(cal(moved))


def cycle(lst, times):
    saved = []
    cyc = None
    i = None
    for i in range(times):
        for way in ['N', 'W', 'S', 'E']:
            lst = move_rock(lst, way)
        if lst in saved:
            cyc = i - saved.index(lst)
            break
        else:
            saved.append(deepcopy(lst))
    if cyc:
        remain = (times - i - 1) % cyc
        for j in range(remain):
            for way in ['N', 'W', 'S', 'E']:
                lst = move_rock(lst, way)

    return lst


moved2 = cycle(st, 1000000000)
print(cal(moved2))


