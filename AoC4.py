import AOCH
from operator import itemgetter

input4 = AOCH.passport('input4.txt')


def run(input_list):
    list_att = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    count_t = 0
    input_list = sorted(input_list, key=itemgetter(1))
    temp5 = []

    for i in input_list:
        if len(i) < len(list_att) - 1:
            continue

        count_att = 0

        for j in range(len(i)):
            if i[j][0] in list_att:
                count_att += 1
            if count_att == len(list_att):
                count_t += 1
                temp5.append(i)
    return [count_t, temp5]


print('Part 1: ' + str(run(input4)[0]))


def run2(input_list):
    temp5 = run(input_list)[1]

    list_att2 = {'byr': ['bt', [1920, 2002]],
                 'iyr': ['bt', [2010, 2020]],
                 'eyr': ['bt', [2020, 2030]],
                 'hgt': ['et', {'cm': [150, 193],
                                'in': [59, 76]}],
                 'hcl': ['fs', ['#', 6]],
                 'ecl': ['e', ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']],
                 'pid': ['l', 9],
                 'cid': ['c']}

    count_t = 0
    for i in temp5:
        valid = True
        for j in i:
            if list_att2[j[0]][0] == 'bt':
                if int(j[1]) not in range(list_att2[j[0]][1][0], list_att2[j[0]][1][1] + 1):
                    valid = False
                    break
            elif list_att2[j[0]][0] == 'et':
                if j[1][-2:] not in ['cm', 'in']:
                    valid = False
                    break
                if int(j[1][:-2]) not in range(list_att2[j[0]][1][j[1][-2:]][0], list_att2[j[0]][1][j[1][-2:]][1] + 1):
                    valid = False
                    break
            elif list_att2[j[0]][0] == 'fs':
                if j[1][0] != '#':
                    valid = False
                    break
                for k in j[1][1:]:
                    if k not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                        valid = False
                        break
            elif list_att2[j[0]][0] == 'e':
                if j[1] not in list_att2[j[0]][1]:
                    valid = False
                    break
            elif list_att2[j[0]][0] == 'l':
                if len(j[1]) != list_att2[j[0]][1]:
                    valid = False
                    break
        if valid:
            count_t += 1

    return count_t


print('Part 2: ' + str(run2(input4)))
