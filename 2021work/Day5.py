from collections import Counter
ind = [line.split(' -> ') for line in [lines.rstrip('\n') for lines in open('input5.txt')]]


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


def run(input_list, task=1):
    inter = Counter()
    for l in input_list:
        x1, x2, y1, y2 = get_xy(l)
        if x1 == x2:
            for i in range(abs(y1 - y2) + 1):
                inter['{},{}'.format(x1, min(y1, y2) + i)] += 1
        elif y1 == y2:
            for i in range(abs(x1 - x2) + 1):
                inter['{},{}'.format(min(x1, x2) + i, y1)] += 1
        elif x1 != x2 and y1 != y2 and task == 2:
            for i in range(abs(x1 - x2) + 1):
                a = calc_a(l)
                if x1 < x2:
                    inter['{},{}'.format(x1 + i, y1 + i * a)] += 1
                elif x1 > x2:
                    inter['{},{}'.format(x1 - i, y1 - i * a)] += 1
    print(sum(i >= 2 for i in inter.values()))


run(ind, 1)
run(ind, 2)


