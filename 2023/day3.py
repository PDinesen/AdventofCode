from regex import findall
import copy

st1 = [item for item in [contents.rstrip('\n') for contents in open('input/' + 'day3' + '.txt')]]

num = [str(i) for i in range(10)]

st = copy.deepcopy(st1)

def adjecten(number, i, lst):
    ind = lst[i].index(number)
    for col in range(-1, len(number) + 1):
        for row in range(-1, 2):
            if 0 <= ind + col < len(lst[i]) and 0 <= i + row < len(lst):
                if lst[i + row][ind + col] not in num and lst[i + row][ind + col] != '.':
                    return True
    return False


def adj(pos_r, pos_c, lst):
    rest = []
    for row in range(-1, 2):
        for col in range(-1, 2):
            if 0 <= pos_c + col < len(lst[pos_r]) and 0 <= pos_r + row < len(lst):
                print(lst[pos_r + row][pos_c + col])
                if lst[pos_r + row][pos_c + col] in num:
                    t = list(map(int, findall(r'\d+', lst[pos_r + row][pos_c + col - 2: pos_c + col + 3])))
                    print(t)
                    if max(t) not in rest:
                        rest.append(max(t))
    return rest

res = 0

for i in range(len(st)):
    temp = findall(r'\d+', st[i])
    for numb in temp:
        if adjecten(numb, i, st):
            res += int(numb)
        st[i] = st[i].replace(numb, '.' * len(numb), 1)

print(res)
res2 = 0
for i in range(len(st1)):
    for j in range(len(st1[0])):
        if st1[i][j] == '*':
            sett = adj(i, j, st1)
            print(sett)
            if len(sett) == 2:
                print('her')
                res2 += int(sett[0]) * int(sett[1])
print(res2)



