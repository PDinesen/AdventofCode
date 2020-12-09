import AOCH

test = AOCH.ril('input7.txt')

print(test)
temp = []
for line in test:
    temp.append(line.split(' '))

testint = [str(i) for i in range(1, 10)]
print(testint)
print(temp)
temp2 = {}
temp3 = []
for i in temp:
    temp3 = []
    for j in range(3, len(i)):
        if i[j][:3] == 'bag' or i[j] == 'bags':
            temp3.append([i[j-3], i[j-2] + ' ' + i[j-1]])
    temp2[i[0] + ' ' + i[1]] = temp3

print(temp2)
testfor = 'shiny gold'



def run(myset, testfor):
    goodbags = [testfor]
    for item in goodbags:
        for keyval in myset:
            if item in myset[keyval] and keyval not in goodbags:
                goodbags.append(keyval)

    return len(goodbags)-1


print(run(temp2, testfor))


def run2(myset, testfor):
    count = 0
    for bag in myset[testfor]:
        if bag[0] == 'contain':
            continue
        print(bag)
        count += int(bag[0]) + int(bag[0])*run2(myset, bag[1])
    return count


print((run2(temp2,testfor)))
