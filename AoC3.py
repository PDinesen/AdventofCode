import AOCH

input3 = AOCH.ril("input3.txt")


def run(list_name: list, position: list, x: int, y: int):
    pos = position
    count1 = 0
    l = len(list_name[pos[0]])
    in_scope = True
    while in_scope:
        pos[1] = pos[1] % l
        if list_name[pos[0]][pos[1]] == '#':
            count1 += 1
        pos[0] += x
        pos[1] += y
        if pos[0] >= len(list_name):
            in_scope = False
    return count1


directions = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
res = 1
for i in directions:
    temp = run(input3, [0, 0], i[0], i[1])
    print(i, temp)
    res *= temp

print('Result part 2 ' + str(res))
