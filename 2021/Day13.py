ind = [item.split() for item in [line.rstrip('\n') for line in open('input13.txt')]]
print(ind)
temp1 = set()
folding = []
for item in ind:
    if len(item) == 1:
        temp1.add(tuple(map(int, item[0].split(','))))
    elif len(item) == 3:
        folding.append(item[-1])

print(temp1, folding)

def fold(ins, ind):
    line = int(ins.split('=')[-1])
    temp = ind.copy()
    if ins[0] == 'x':
        for item in ind:
            x1, y1 = item
            if x1 > line:
                x1 = line - (x1 - line)
                temp.remove(item)
                temp.add((x1, y1))
    elif ins[0] == 'y':
        for item in ind:
            x1, y1 = item
            if y1 > line:
                y1 = line - (y1 - line)
                temp.remove(item)
                temp.add((x1, y1))
    return temp

test = fold(folding[0], temp1)
print(len(test), test)
print(fold(folding[1], test))

def run(ins_list, ind):
    temp = ind.copy()
    for ins in ins_list:
        temp = fold(ins, temp)
        print(len(temp))
    return temp

temp = run(folding, temp1)

minx, maxx = min(x[0] for x in temp), max(x[0] for x in temp)
miny, maxy = min(x[1] for x in temp), max(x[1] for x in temp)

for i in range(miny, maxy + 1):
    temp2 = ''
    for j in range(minx, maxx + 1):
        if (j, i) in temp:
            temp2 += '#'
        else:
            temp2 += ' '
    print(temp2)