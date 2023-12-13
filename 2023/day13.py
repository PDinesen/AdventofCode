from copy import deepcopy
st = [contents.rstrip('\n') for contents in open('input/' + 'day13' + '.txt')]

maps = []
temp = []
for line in st:
    if line == '':
        maps.append(temp)
        temp = []
    else:
        temp.append(line)
maps.append(temp)


def find_row(m, not_row=-1):
    for i in range(len(m) - 1):
        if i == not_row - 1:
            continue
        find = True
        for j in range(min(i + 1, len(m) - i - 1)):
            if m[i - j] != m[i + j + 1]:
                find = False
                break
        if find:
            return i + 1
    return 0


def find_col(m, not_col=-1):
    length = len(m[0]) - 1
    for i in range(length):
        if i == not_col - 1:
            continue
        size = min(i + 1, length - i)
        find = True
        for j in range(len(m)):
            if m[j][i - (size - 1): i + 1] != m[j][i + 1: i + size + 1][::-1]:
                find = False
                break
        if find:
            return i + 1
    return 0


def part2(m):
    row = find_row(m)
    col = find_col(m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            t = deepcopy(m)
            if t[i][j] == '#':
                t[i] = t[i][:j] + '.' + t[i][j+1:]
            else:
                t[i] = t[i][:j] + '#' + t[i][j + 1:]
            if find_row(t, row) != 0:
                return find_row(t, row) * 100
            elif find_col(t, col) != 0:
                return find_col(t, col)


def solution(lst):
    res = 0
    for m in lst:
        res += 100 * find_row(m) + find_col(m)
    return res


print(solution(maps))


def solution2(lst):
    res = 0
    for m in lst:
        res += part2(m)
    return res


print(solution2(maps))
