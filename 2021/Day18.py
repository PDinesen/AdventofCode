from ast import literal_eval

ind = [line.rstrip('\n') for line in open('input18.txt')]
print(literal_eval(ind[0] + ',' + ind[1]))
ind = list(map(literal_eval, ind))


def explode(tree, depth=0):
    if isinstance(tree, list):
        l, r = tree
        if depth >= 4:
            return 0, True, l, r
        else:
            l, reduced, expl, expr = explode(l, depth + 1)
            if reduced:
                if expr != 0:
                    r = add_left(r, expr)
                    expr = 0
            else:
                r, reduced, expl, expr = explode(r, depth + 1)
                if reduced:
                    if expl != 0:
                        l = add_right(l, expl)
                        expl = 0
            if reduced:
                return [l, r], True, expl, expr
    return tree, False, 0, 0


def add_left(n, m):
    if isinstance(n, int):
        return n + m
    else:
        a, b = n
        return [add_left(a, m), b]


def add_right(n, m):
    if isinstance(n, int):
        return n + m
    else:
        a, b = n
        return [a, add_right(b, m)]


print(explode([[[[[9,8],1],2],3],4]))

test1 = explode([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]])[0]
test2 = explode(test1)[0]


def split(tree):
    if isinstance(tree, int):
        if tree > 9:
            return [tree // 2, tree - tree // 2], True
    else:
        l, r = tree
        l, split_l = split(l)
        if split_l:
            return [l, r], True
        r, split_r = split(r)
        if split_r:
            return [l, r], True
        return [l, r], False
    return tree, False

test3 = split(test2)[0]
test4 = split(test3)[0]
print(explode(test4)[0])


def reduce(tree):
    exploded, splitted = True, True
    while exploded or splitted:
        tree, exploded, _, _ = explode(tree)
        if exploded:
            continue
        tree, splitted = split(tree)
    return tree


def run(ind):
    start = reduce(ind[0])
    for item in ind[1:]:
        start = reduce([start, item])
    return start


print(run(ind))
print([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])


def magnitude(tree):
    if isinstance(tree, int):
        return tree
    else:
        l, r = tree
        return 3 * magnitude(l) + 2 * magnitude(r)

print(magnitude(run(ind)))

def run2(ind):
    mag = 0
    for i in range(len(ind)):
        for j in range(len(ind)):
            if i != j:
                ans = magnitude(run([ind[i], ind[j]]))
                if ans > mag:
                    mag = ans
    return mag

print(run2(ind))















