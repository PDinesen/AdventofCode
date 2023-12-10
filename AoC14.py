import AOCH


def split_in_list(filename):
    temp = AOCH.ril(filename)
    temp2 = []
    temp3 = []
    mask = ''
    for i in range(len(temp)):
        if temp[i].split(' = ')[0] == 'mask':
            if len(mask) > 0:
                temp3.append([mask, temp2])
            mask = temp[i].split(' = ')[1]
            temp2 = []
        else:
            if temp[i][:3] == 'mem':
                temp2.append([int(temp[i].split(' = ')[0][4:-1]), int(temp[i].split(' = ')[1])])
    temp3.append([mask, temp2])
    return temp3


input14 = split_in_list('test.txt')


def run(input_list):
    list_name = input_list.copy()
    res_set = {}
    for item in list_name:
        mask = item[0]
        for memory in item[1]:
            memory[1] = bin(memory[1])[2:]
            memory[1] = '0' * (len(mask) - len(memory[1])) + memory[1]
            """
            print('--------------------------------------')
            print('value = ' + str(int(memory[1], 2)) + ' to memory index ' + str(memory[0]))
            print('value  ' + memory[1])
            print('mask   ' + mask)
            """
            for b in range(1, len(mask)+1):
                if mask[-b] != 'X':
                    if b == 1:
                        memory[1] = memory[1][:-b] + mask[-b]
                    elif b == len(mask)-1:
                        memory[1] = mask[-b] + memory[1][-b+1:]
                    else:
                        memory[1] = memory[1][:-b] + mask[-b] + memory[1][-b + 1:]
            # print('result ' + memory[1])
            res_set[memory[0]] = int(memory[1], 2)
            # print('value = ' + str(int(memory[1], 2)) + ' to memory index ' + str(memory[0]))

    return res_set


res = run(input14)
the_sum = 0
for key in res:
    the_sum += res[key]

print(the_sum)


def all_addresses(item):
    index = 0
    res = ['']
    for i in range(len(item)):
        if item[i] != 'X':
            for j in range(len(res)):
                res[j] += item[i]
        else:
            lenght = len(res)
            temp = res.copy()
            for j in range(lenght):
                res[j] += '0'
            for j in range(lenght):
                res.append(temp[j] + '1')
    for i in range(len(res)):
        res[i] = int(res[i], 2)
    return res


def change_string(string_item, index, value):
    if index == 1:
        return string_item[:-index] + value
    elif index == len(string_item) - 1:
        return value + string_item[-index + 1:]
    else:
        return string_item[:-index] + value + string_item[-index + 1:]


def run2(list_name):
    res_set = {}
    for item in list_name:
        mask = item[0]
        print(item)
        for memory in item[1]:
            memory[0] = bin(memory[0])[2:]
            memory[0] = '0'*(len(mask) - len(memory[0])) + memory[0]
            for b in range(1, len(mask)+1):
                if mask[-b] == 'X':
                    memory[0] = change_string(memory[0], b, 'X')
                elif mask[-b] == '1':
                    memory[0] = change_string(memory[0], b, '1')
            for memory_input in all_addresses(memory[0]):
                res_set[memory_input] = memory[1]

    return res_set

input14 = split_in_list('input14.txt')
sum2 = 0
res = run2(input14)
for key in res:
    sum2 += res[key]

print(sum2)