import AOCH

input5 = AOCH.ril("input5.txt")


def run(input_list):

    maxi = 0
    ID = []
    for i in input_list:
        row = ''
        col = ''

        for j in i:
            if j == 'F':
                row += '0'
            elif j == 'B':
                row += '1'
            elif j == 'R':
                col += '1'
            elif j == 'L':
                col += '0'

        if int(row, 2) * 8 + int(col, 2) > maxi:
            maxi = int(row, 2) * 8 + int(col, 2)

        ID.append(int(row, 2) * 8 + int(col, 2))

    ID = sorted(ID)
    res = -1
    for i in range(min(ID), max(ID)):
        if i not in ID:
            res = i
            break

    return [maxi, res]


result = run(input5)
print('Part 1: ' + str(result[0]) + '.\n' + 'Part 2: ' + str(result[1]) + '.')
