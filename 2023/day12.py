st = [contents.rstrip('\n').split(' ') for contents in open('input/' + 'day12' + '.txt')]
st = [[x[0], list(map(int, x[1].split(',')))] for x in st]

save = {}


def recursive(grp: str, dmg: list, i: int = 0, dmgi=0, curr=0):
    key = (i, dmgi, curr)
    if key in save:
        return save[key]
    if i == len(grp):
        if dmgi == len(dmg) and curr == 0:
            return 1
        elif dmgi == len(dmg) - 1 and dmg[dmgi] == curr:
            return 1
        else:
            return 0
    ans = 0
    for c in ['.', '#']:
        if grp[i] in c + '?':
            if c == '.' and curr == 0:
                ans += recursive(grp, dmg, i + 1, dmgi, 0)
            elif c == '.' and curr > 0 and dmgi < len(dmg) and dmg[dmgi] == curr:
                ans += recursive(grp, dmg, i + 1, dmgi + 1, 0)
            elif c == '#':
                ans += recursive(grp, dmg, i + 1, dmgi, curr + 1)

    save[key] = ans
    return ans


res = 0
for line in st:
    save.clear()
    res += recursive(line[0], line[1])
print(res)

res2 = 0
for line in st:
    save.clear()
    res2 += recursive('?'.join(line[0] for _ in range(5)), line[1] * 5)
print(res2)
