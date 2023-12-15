test_res = 1320

st = [contents.rstrip('\n') for contents in open('input/' + 'day15' + '.txt')][0].split(',')

print(st)


def get_ascii(s: str):
    t = 0
    for i in s:
        t = ((t + ord(i)) * 17) % 256
    return t


res = 0
for se in st:
    res += get_ascii(se)

print(res)



def make_box(lst):
    box = {}
    for ins in lst:
        if '-' in ins:
            box_number = get_ascii(ins[:-1])
            if box_number in box.keys():
                for i in range(len(box[box_number])):
                    if box[box_number][i][0] == ins[:-1]:
                        box[box_number].pop(i)
                        break
                if len(box[box_number]) == 0:
                    del box[box_number]
        elif '=' in ins:
            inss, focal = ins.split('=')
            box_number = get_ascii(inss)
            focal = int(focal)
            if box_number in box.keys():
                if inss in [x[0] for x in box[box_number]]:
                    for i, j in enumerate(box[box_number]):
                        if j[0] == inss:
                            box[box_number][i][1] = focal
                            break
                else:
                    box[box_number].append([inss, focal])
            else:
                box[box_number] = [[inss, focal]]
    return box


def cal(lst):
    box = make_box(lst)
    res2 = 0
    for k in box.keys():
        res2 += (k + 1) * sum((i + 1)*el[1] for i, el in enumerate(box[k]))
    return res2


print(cal(st))

