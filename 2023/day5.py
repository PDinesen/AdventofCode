import copy

st = [item for item in [contents.rstrip('\n') for contents in open('input/' + 'day5' + '.txt')]]


def initial(part1=True):
    save = dict()
    temp = list(map(int, st[0].split(':')[1].split()))
    if not part1:
        temp2 = [(temp[i], temp[i] + temp[i + 1] - 1) for i in range(len(temp)) if i % 2 == 0]
        temp = temp2

    save['seed'] = temp


    maps = dict()
    mapt = []
    start = True
    for line in st[2::]:
        if start:
            ID = line.split()[0].split('-')[2]
            start = False
        elif not line:
            maps[ID] = mapt
            mapt = []
            start = True
        else:
            mapt.append(list(map(int, line.split())))
    maps[ID] = mapt

    return save, maps

def solve(part1=True):
    save, maps = initial(part1)
    if part1:
        prev = 'seed'
        for item in maps.keys():
            temp = copy.deepcopy(save[prev])
            for i in range(len(temp)):
                for ma in maps[item]:
                    if ma[1] <= temp[i] < ma[1] + ma[2]:
                        temp[i] += ma[0] - ma[1]
                        break
            save[item] = temp
            prev = item
        print(min(save['location']))
    else:
        locations = []
        for par in save['seed']:
            remain = [par]
            result = []
            for item in maps.keys():
                while remain:
                    prev = remain.pop()
                    for ma in maps[item]:
                        move = ma[0] - ma[1]
                        a = ma[1]
                        b = ma[1] + ma[2] - 1
                        if prev[0] > b or prev[1] < a:
                            continue
                        elif a <= prev[0]:
                            if prev[1] <= b:
                                result.append((prev[0] + move, prev[1] + move))
                                break
                            else:
                                result.append((prev[0] + move, b + move))
                                remain.append((b + 1, prev[1]))
                                break
                        else:
                            if prev[1] <= b:
                                result.append((a + move, prev[1] + move))
                                remain.append((prev[0], a - 1))
                                break
                            else:
                                result.append((a + move, b + move))
                                remain.append((prev[0], a - 1))
                                remain.append((b + 1, prev[1]))
                                break
                    else:
                        result.append(prev)
                remain = result
                result = []
            locations.extend(remain)
        print(min(i[0] for i in locations))


if __name__=='__main__':
    solve()
    solve(False)

