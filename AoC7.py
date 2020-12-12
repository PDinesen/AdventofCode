import AOCH

input7 = AOCH.ril('input7.txt')
input7 = AOCH.split_by(input7, ' ')


def make_set(input_list):
    temp2 = {}
    for i in input_list:
        temp3 = []
        for j in range(3, len(i)):
            if i[j][:3] == 'bag' or i[j] == 'bags':
                temp3.append([i[j - 3], i[j - 2] + ' ' + i[j - 1]])
        temp2[i[0] + ' ' + i[1]] = temp3
    return temp2


input7 = make_set(input7)

test_for1 = 'shiny gold'


def run(my_set, test_for):
    good_bags = [test_for]
    for item in good_bags:
        for key_val in my_set:
            test_list = [bag[1] for bag in my_set[key_val]]
            if item in test_list and key_val not in good_bags:
                good_bags.append(key_val)
    return len(good_bags) - 1


print(run(input7, test_for1))


def run2(my_set, test_for):
    count = 0
    for bag in my_set[test_for]:
        if bag[0] == 'contain':
            continue
        count += int(bag[0]) + int(bag[0]) * run2(my_set, bag[1])
    return count


print((run2(input7, test_for1)))
