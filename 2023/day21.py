import time
import numpy as np

st = [list(line) for line in [c.rstrip('\n') for c in open('input/' + 'day21' + '.txt')]]

offset = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def find_start(lst):
    for i, r in enumerate(lst):
        for j, c in enumerate(r):
            if c == 'S':
                return i, j


def move(f, lst):
    t = []
    r, c = f
    for dr, dc in offset:
        rt = (r + dr) % len(lst)
        ct = (c + dc) % len(lst[0])
        if lst[rt][ct] in 'S.':
            t.append((r + dr, c + dc))
    return t


def print_garden(lst, v):
    print('')
    for i, r in enumerate(lst):
        print(''.join(c if (i, j) not in v else 'O' for j, c in enumerate(r)))


def run(lst, times=64, part2=False):
    s = find_start(lst)
    q = {s}
    even = set()
    odd = set()
    xx, yy = [0, 1, 2], []
    if part2:
        times = len(lst) // 2 + len(lst) * max(xx) + 1
    for i in range(times):
        if i % len(lst) == len(lst) // 2:
            if i % 2 == 0:
                yy.append(len(even) + len(q))
            else:
                yy.append(len(odd) + len(q))
        if i == 64:
            print('answer part 1: ', len(even) + len(q))
        tq = set()
        if i % 2 == 0:
            for new in q:
                even.add(new)
            while q:
                f = q.pop()
                for new in move(f, lst):
                    if new not in odd:
                        tq.add(new)
        else:
            for new in q:
                odd.add(new)
            while q:
                f = q.pop()
                for new in move(f, lst):
                    if new not in even:
                        tq.add(new)
        q = tq

    if part2:
        poly = np.polyfit(xx, yy, 2)[::-1]
        n = (26501365 - len(lst) // 2) // len(lst)
        res = sum(poly[i] * (n ** i) for i in range(3))
        print('answer part 2: ', round(res))


ts = time.time()
run(st, part2=True)
print(time.time() - ts)
