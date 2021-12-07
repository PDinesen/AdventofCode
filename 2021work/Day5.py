ind = [line.split(' -> ') for line in [lines.rstrip('\n') for lines in open('input5.txt')]]

def calc_intersect_int(l1, l2):
    a1 = calc_a(l1)
    a2 = calc_a(l2)


def calc_a(l):
    y1, y2 = (int(l[0].split(',')[1]), int(l[1].split(',')[1]))
    x1, x2 = (int(l[0].split(',')[0]), int(l[1].split(',')[0]))
    return int((y2-y1)/(x2-x1))

def v_h_check(l):
    y1, y2 = (l[0].split(',')[1], l[1].split(',')[1])
    x1, x2 = (l[0].split(',')[0], l[1].split(',')[0])
    return y1 == y2 or x1 == x2

def get_xy(l):
    y1, y2 = (int(l[0].split(',')[1]), int(l[1].split(',')[1]))
    x1, x2 = (int(l[0].split(',')[0]), int(l[1].split(',')[0]))
    return (x1, x2, y1, y2)

inter = {}
for l in ind:
    x1, x2, y1, y2 = get_xy(l)
    if x1 == x2:
        for i in range(abs(y1 - y2) + 1):
            try:
                inter['{},{}'.format(x1, min(y1, y2) + i)] += 1
            except:
                inter['{},{}'.format(x1, min(y1, y2) + i)] = 1
    elif y1 == y2:
        for i in range(abs(x1 - x2) + 1):
            try:
                inter['{},{}'.format(min(x1, x2) + i, y1)] += 1
            except:
                inter['{},{}'.format(min(x1, x2) + i, y1)] = 1
    elif x1 != x2 and y1 != y2:
        for i in range(abs(x1 - x2) + 1):
            a = calc_a(l)
            if x1 < x2:
                try:
                    inter['{},{}'.format(x1 + i, y1 + i * a)] += 1
                except:
                    inter['{},{}'.format(x1 + i, y1 + i * a)] = 1
            elif x1 > x2:
                try:
                    inter['{},{}'.format(x1 - i, y1 - i * a)] += 1
                except:
                    inter['{},{}'.format(x1 - i, y1 - i * a)] = 1







print(v_h_check(ind[1]))
print(ind)
print(sum(i >= 2 for i in inter.values()))


print('1,{}'.format(1+2))