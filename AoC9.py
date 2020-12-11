import AOCH

input9 = AOCH.ril('input9.txt')


input9 = list(map(int, input9))


def val_list(item_list):
    temp = []
    for i in range(len(item_list)):
        for j in range(len(item_list)):
            temp.append(item_list[i] + item_list[j])
    return temp


def run(item_list, val_int):
    for i in range(val_int, len(item_list)):
        if item_list[i] not in val_list(item_list[i - val_int:i]):
            return item_list[i]
    return 0


def run2(item_list, val_int):
    number = run(item_list, val_int)
    for i in range(len(item_list)):
        for j in range(i):
            if sum(item_list[i - j:i]) == number:
                return min(item_list[i - j:i]) + max(item_list[i-j:i])

    return 0


print('Part 1: ' + str(run(input9, 25)))
print('Part 2: ' + str(run2(input9, 25)))
