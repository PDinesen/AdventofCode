import heapq
from functools import wraps


st = [item for item in [content.rstrip('\n') for content in open('input/' + 'day19' + '.txt')]]


towels = st[0].split(', ')
min_len = min(map(len, towels))
max_len = max(map(len, towels))
request = st[2:]


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]
    return wrapper


@memoize
def try_rec(rest):
    if rest == '':
        return 1
    temp = 0
    for j in range(min_len, max_len + 1):
        if j > len(rest):
            continue
        if rest[:j] in towels:
            temp += try_rec(rest[j:])
    return temp


ans1 = 0
ans2 = 0
for re in request:
    s2 = try_rec(re)
    ans2 += s2
    if s2 > 0:
        ans1 += 1


print(' ')
print(ans1)
print(ans2)
