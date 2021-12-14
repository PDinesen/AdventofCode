
def initial(txt_name):
    ind = [item.split() for item in [line.rstrip('\n') for line in open(txt_name)]]
    temp1 = set()
    folding = []
    for item in ind:
        if len(item) == 1:
            temp1.add(tuple(map(int, item[0].split(','))))
        elif len(item) == 3:
            folding.append(item[-1])
    return folding, temp1


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


def run(txt_name):
    ins_list, ind = initial(txt_name)
    temp = ind.copy()
    for ins in ins_list:
        temp = fold(ins, temp)
        if ins == ins_list[0]:
            print(len(temp))
    return temp


def run2(txt_name):
    temp = run(txt_name)

    min_x, max_x = min(x[0] for x in temp), max(x[0] for x in temp)
    min_y, max_y = min(x[1] for x in temp), max(x[1] for x in temp)

    for i in range(min_y, max_y + 1):
        temp2 = ''
        for j in range(min_x, max_x + 1):
            if (j, i) in temp:
                temp2 += '#'
            else:
                temp2 += ' '
        print(temp2)


if __name__ == '__main__':
    run2('input13.txt')
