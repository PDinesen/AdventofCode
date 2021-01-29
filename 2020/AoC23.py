class Node:
    def __init__(self, number, pred, succ):
        self.n = number
        self.pred = pred
        self.succ = succ


def add_list(lst: list):
    prev = Node(lst[0], None, None)
    first = prev
    n = first
    for element in lst[1:]:
        n = Node(element, prev, None)
        prev.succ = n
        prev = n
    n.succ = first
    first.pred = n
    return first


def to_dict(current: Node):
    d = {}
    n = current.n
    d[n] = current
    while True:
        current = current.succ
        if current.n == n:
            break
        d[current.n] = current
    return d


def to_list(current: Node):
    first = current.n
    res = [first]
    while True:
        current = current.succ
        if current.n == first:
            break
        res.append(current.n)
    return res


def make_move(curr, d, l):
    first = curr
    pick1 = curr.succ
    pick2 = pick1.succ
    pick3 = pick2.succ

    curr.succ = pick3.succ
    pick3.pred = curr

    n = curr.n
    while True:
        n -= 1
        if n == 0:
            n = l
        if n not in [pick1.n, pick2.n, pick3.n]:
            break

    curr = d[n]

    k = curr.succ
    curr.succ = pick1
    pick1.pred = curr
    pick3.succ = k
    k.pred = pick3
    return first.succ


for is_part1 in [True, False]:
    n = [int(i) for i in "853192647"]

    if is_part1:
        n_moves = 100
    else:
        n += list(range(10, 1000001))
        n_moves = 10000000

    l = len(n)
    n = add_list(n)
    d = to_dict(n)

    for move in range(n_moves):
        n = make_move(n, d, l)
    k = to_list(d[1])
    if is_part1:
        print("".join(str(c) for c in k[1:]))
    else:
        print(k[1]*k[2])
