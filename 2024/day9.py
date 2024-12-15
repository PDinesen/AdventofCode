st = [item for item in [contents.rstrip('\n') for contents in open('input/' + 'day9' + '.txt')]]
st = st[0]

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
blocks = []
free_blocks = []
for i in range(len(files)):
    blocks.append((counter, i, int(files[i])))
    counter += int(files[i])
    if i < len(free) and free[i] != '0':
        free_blocks.append([counter, int(free[i])])
        counter += int(free[i])

blocks_new = blocks.copy()
for i in range(len(blocks) - 1, -1, -1):
    index, number, times = blocks[i]
    if i != number:
        continue
    for j in range(len(free_blocks)):
        index_free, times_free = free_blocks[j]
        if index_free >= index:
            break
        if times <= times_free:
            blocks_new.remove(blocks[i])
            blocks_new.append((index_free, number, times))
            if times == times_free:
                free_blocks.pop(j)
            else:
                free_blocks[j] = [index_free + times, times_free - times]
            free_blocks.append([index, times])
            free_blocks.sort(key=lambda x: x[0])
            for k in range(len(free_blocks) - 1):
                if sum(free_blocks[k]) == free_blocks[k + 1][0]:
                    free_blocks[k] = [free_blocks[k][0], free_blocks[k][1] + free_blocks[k + 1][1]]
                    free_blocks.pop(k + 1)
                    break
            break

blocks_new.sort()
checksum = 0
for index, amount, times in blocks_new:
    for _ in range(times):
        checksum += index * amount
        index += 1

print(checksum)
