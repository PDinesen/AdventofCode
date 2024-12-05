st = [item for item in [contents.rstrip('\n') for contents in open('input/' + 'day1' + '.txt')]]
arr1 = []
arr2 = []
for item in st:
    temp = item.split(' ')
    arr1.append(int(temp[0]))
    arr2.append(int(temp[-1]))

arr1.sort()
arr2.sort()

s = 0
s2 = 0
print(len(arr1))
for el in zip(arr1, arr2):
    s += abs(el[0]-el[1])
    s2 += el[0] * arr2.count(el[0])

print(s)
print(s2)


