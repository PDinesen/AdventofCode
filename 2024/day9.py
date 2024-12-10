st = [item for item in [contents.rstrip('\n') for contents in open('input/' + 'day9' + '.txt')]]
st = st[0]
##st = '2333133121414131402'

files = st[::2]
free = st[1::2]

k = len(files) - 1
res = 0
counter = 0
for i in range(len(files)):
    for _ in range(int(files[i])):
        res += i * counter
        counter += 1
    files = files[:i] + '0' + files[i + 1:]
    if i < len(free):
        for j in range(int(free[i])):
            while k > -1:
                if files[k] != '0':
                    files = files[:k] + str(int(files[k]) - 1) + files[k + 1:]
                    res += k * counter
                    counter += 1
                    break
                else:
                    k -= 1


print(res)

files = st[::2]
free = st[1::2]


res = 0
counter = 0
line = ''
bloks = []
free_bloks = []
for i in range(len(files)):
    bloks.append((counter, i, int(files[i])))
    counter += int(files[i])
    if i < len(free) and free[i] != '0':
        free_bloks.append([counter, int(free[i])])
        counter += int(free[i])

print(bloks, free_bloks)
bloks_new = bloks.copy()
for i in range(len(bloks) - 1, -1, -1):
    index, number, times = bloks[i]
    if i != number:
        continue
    for j in range(len(free_bloks)):
        index_free, times_free = free_bloks[j]
        if index_free >= index:
            break
        if times <= times_free:
            bloks_new.remove(bloks[i])
            bloks_new.append((index_free, number, times))
            if times == times_free:
                free_bloks.pop(j)
            else:
                free_bloks[j] = [index_free + times, times_free - times]
            free_bloks.append([index, times])
            free_bloks.sort(key=lambda x:x[0])
            for k in range(len(free_bloks) - 1):
                if sum(free_bloks[k]) == free_bloks[k + 1][0]:
                    free_bloks[k] = [free_bloks[k][0], free_bloks[k][1] + free_bloks[k + 1][1]]
                    free_bloks.pop(k + 1)
                    break
            break
bloks_new.sort()
checksum = 0
for index, amount, times in bloks_new:
    for _ in range(times):
        checksum += index * amount
        index += 1
print(checksum)





print(res)
print(line)