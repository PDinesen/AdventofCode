import AOCH

input9 = AOCH.ril('input9.txt')

print(input9)


def int_list(item_list):
    temp = []
    for i in range(len(item_list)):
        temp.append(int(item_list[i]))
    return temp


input9 = int_list(input9)


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


def test(val_list1, test1):
    temp = []
    for i in val_list1:
        temp.append(i - test1)
    return temp


def sum_f(item_list):
    sum_1 = 0
    for i in item_list:
        sum_1 += i

    return sum_1


def smallest_larges(item_list):
    sm = item_list[0]
    lar = item_list[0]
    for i in item_list:
        if i < sm:
            sm = i
        elif i > lar:
            lar = i
    return sm + lar


print(smallest_larges([10, 20, 30]))


def run2(item_list, val_int):
    number = run(item_list, val_int)
    for i in range(len(item_list)):
        for j in range(i):
            if sum_f(item_list[i - j:i]) == number:
                return smallest_larges(item_list[i - j:i])

    return 0


print(run(input9, 25))
print(run2(input9, 25))
