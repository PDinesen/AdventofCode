import AOCH

test = AOCH.ril('input7.txt')

print(test)
temp = []
for line in test:
    temp.append(line.split(' '))

test_int = [str(i) for i in range(1, 10)]
print(test_int)
print(temp)
temp2 = {}
temp3 = []
for i in temp:
    temp3 = []
    for j in range(3, len(i)):
        if i[j][:3] == 'bag' or i[j] == 'bags':
            temp3.append([i[j - 3], i[j - 2] + ' ' + i[j - 1]])
    temp2[i[0] + ' ' + i[1]] = temp3

print(temp2)
test_for1 = 'shiny gold'


def run(my_set, test_for):
    good_bags = [test_for]
    for item in good_bags:
        for key_val in my_set:
            if item in my_set[key_val] and key_val not in good_bags:
                good_bags.append(key_val)

    return len(good_bags) - 1


print(run(temp2, test_for1))


def run2(my_set, test_for):
    count = 0
    for bag in my_set[test_for]:
        if bag[0] == 'contain':
            continue
        print(bag)
        count += int(bag[0]) + int(bag[0]) * run2(my_set, bag[1])
    return count


print((run2(temp2, test_for1)))
