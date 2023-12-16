from time import time

start_time = 1702726813.5130277

st = [contents.rstrip('\n') for contents in open('input/' + 'day16' + '.txt')]
s = (0, -1, 'r')

def find_energy(lst, start_que):

    que = [start_que]
    visit = set()
    count = 0
    remember = set()
    while len(que) != 0:
        count += 1
        row, col, way = que.pop()
        if (row, col, way) not in remember:
            remember.add((row, col, way))
            if way == 'r':
                if col + 1 < len(lst[0]):
                    visit.add((row, col + 1))
                    if lst[row][col + 1] in '.-':
                        que.append((row, col + 1, 'r'))
                    elif lst[row][col + 1] == '|':
                        que.append((row, col + 1, 'u'))
                        que.append((row, col + 1, 'd'))
                    elif lst[row][col + 1] == '/':
                        que.append((row, col + 1, 'u'))
                    elif lst[row][col + 1] == '\\':
                        que.append((row, col + 1, 'd'))
            elif way == 'l':
                if col - 1 >= 0:
                    visit.add((row, col - 1))
                    if lst[row][col - 1] in '.-':
                        que.append((row, col - 1, 'l'))
                    elif lst[row][col - 1] == '|':
                        que.append((row, col - 1, 'u'))
                        que.append((row, col - 1, 'd'))
                    elif lst[row][col - 1] == '/':
                        que.append((row, col - 1, 'd'))
                    elif lst[row][col - 1] == '\\':
                        que.append((row, col - 1, 'u'))
            elif way == 'u':
                if row - 1 >= 0:
                    visit.add((row - 1, col))
                    if lst[row - 1][col] in '.|':
                        que.append((row - 1, col, 'u'))
                    elif lst[row - 1][col] == '-':
                        que.append((row - 1, col, 'r'))
                        que.append((row - 1, col, 'l'))
                    elif lst[row - 1][col] == '/':
                        que.append((row - 1, col, 'r'))
                    elif lst[row - 1][col] == '\\':
                        que.append((row - 1, col, 'l'))
            elif way == 'd':
                if row + 1 < len(lst):
                    visit.add((row + 1, col))
                    if lst[row + 1][col] in '.|':
                        que.append((row + 1, col, 'd'))
                    elif lst[row + 1][col] == '-':
                        que.append((row + 1, col, 'l'))
                        que.append((row + 1, col, 'r'))
                    elif lst[row + 1][col] == '/':
                        que.append((row + 1, col, 'l'))
                    elif lst[row + 1][col] == '\\':
                        que.append((row + 1, col, 'r'))
    return len(visit)


print(find_energy(st, (0, -1, 'r')))


def solution2(lst):
    m = 0
    for i in range(len(lst)):
        m = max(find_energy(lst, (i, -1, 'r')), m)
        m = max(find_energy(lst, (len(lst) - i - 1, len(lst[0]), 'l')), m)
    for i in range(len(lst[0])):
        m = max(find_energy(lst, (-1, i, 'd')), m)
        m = max(find_energy(lst, (len(lst) - 1, len(lst[0]) - i - 1, 'l')), m)
    return m


print(solution2(st))
print((time() - start_time)//60)

