from math import prod
st = [x.split(' -> ') for x in [c.rstrip('\n') for c in open('input/' + 'day20' + '.txt')]]


def parse_data(lst):
    modules = dict()
    ff = dict()
    cm = dict()
    cm_recieved = dict()

    for l in lst:
        if l[0][0] == '%':
            modules[l[0][1:]] = l[1].split(', ')
            ff[l[0][1:]] = [False, 'low']
        elif l[0][0] == '&':
            modules[l[0][1:]] = l[1].split(', ')
            cm[l[0][1:]] = []
            cm_recieved[l[0][1:]] = 'low'
        else:
            modules[l[0]] = l[1].split(', ')
    for m in modules:
        for to in modules[m]:
            if to in cm:
                cm[to].append(m)

    return modules, ff, cm, cm_recieved


def run_module(pulse, m, all_modules, flip_flop, conjecture, con_):
    ret = []
    if m not in all_modules:
        return ret

    if m in flip_flop:
        if pulse == 'low':
            if flip_flop[m][0]:
                flip_flop[m] = [False, 'low']
                for to in all_modules[m]:
                    ret.append(['low', to])
            else:
                flip_flop[m] = [True, 'high']
                for to in all_modules[m]:
                    ret.append(['high', to])
    elif m in conjecture:
        if all(flip_flop[x][1] == 'high' if x in flip_flop else con_[x] == 'high' for x in conjecture[m]):
            con_[m] = 'low'
            for to in all_modules[m]:
                ret.append(['low', to])
        else:
            con_[m] = 'high'
            for to in all_modules[m]:
                ret.append(['high', to])
    else:
        for to in all_modules[m]:
            ret.append([pulse, to])
    return ret


def solution(lst, times, part1=True):
    m, f, c, cm = parse_data(lst)
    cl = 0
    ch = 0
    count = 0
    if part1:
        while count < times:
            count += 1
            q = [['low', 'broadcaster']]
            while q:
                x = q.pop(0)
                if x[0] == 'low':
                    cl += 1
                else:
                    ch += 1
                q.extend(run_module(x[0], x[1], m, f, c, cm))
            if all(f[i] == [False, 'low'] for i in f):
                print(count)
                t = times // count
                cl *= t
                ch *= t
                count *= t
                print('stop')
        print(cl * ch)
    else:
        run = True
        search = []
        for i in m:
            if 'rx' in m[i]:
                for j in m:
                    if i in m[j]:
                        search.append(j)
        cir = []
        while run:
            count += 1
            q = [['low', 'broadcaster']]
            while q:
                x = q.pop(0)
                if x in [['low', y] for y in search]:
                    cir.append(count)
                    search.remove(x[1])
                if not search:
                    run = False
                if x[0] == 'low':
                    cl += 1
                else:
                    ch += 1
                q.extend(run_module(x[0], x[1], m, f, c, cm))
            if count % 100000 == 0:
                print(count)

        print(prod(cir))




solution(st,1000)
solution(st, 1000, False)

