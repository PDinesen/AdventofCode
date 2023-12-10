import AOCH

input15 = [7, 14, 0, 17, 11, 1, 2]

test = [[1, 3, 2],
        [2, 1, 3],
        [1, 2, 3],
        [2, 3, 1],
        [3, 2, 1],
        [3, 1, 2]]

result = [1, 10, 27, 78, 438, 1836]


def start_set(input_list):
    res = {}
    for i in range(len(input_list)):
        res[input_list[i]] = i + 1

    return res
print(test[0][:-1])



def run(input_list, times):
    temp = input_list.copy()
    while len(temp) < times:
        last_spoken = temp[-1]

        if last_spoken not in temp[:-1]:
            temp.append(0)
        else:
            for i in range(1, len(temp[:-1])+1):
                if temp[:-1][-i] == last_spoken:
                    temp.append(i)
                    break
    return temp


def next_number(set_item: dict, last_number, index):
    if last_number in set_item.keys():
        return index - set_item[last_number]
    else:
        return 0


print(run(input15, 2020))


def run2(input_list, times):
    res_set = start_set(input_list)
    new_spoken = 0
    last_spoken = 0
    index = len(input_list) + 1
    while index <= times:
        last_spoken = new_spoken
        new_spoken = next_number(res_set, last_spoken, index)
        res_set[last_spoken] = index
        index += 1
    return last_spoken


print(run2(input15, 30000000))
"""
for item in test.txt:
    print(run2(item, 2020))
"""