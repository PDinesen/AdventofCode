ind = [line.rstrip('\n') for line in open('input12.txt')]


def initial(input_list):
    temp = {}
    for line in input_list:
        k, v = line.split('-')
        if v != 'start' and k != 'end':
            if k in temp.keys():
                temp[k].append(v)
            else:
                temp[k] = [v]
        if k != 'start' or v != 'end':
            if v in temp.keys():
                temp[v].append(k)
            else:
                temp[v] = [k]
    return temp


def step(path, temp, part2=False):
    ans = []
    for el in temp[path[-1]]:
        temp1 = path.copy()
        if (el not in [item.lower() for item in path] or
            (all(path.count(key) < 2 for key in [item.lower() for item in temp.keys()]) and part2)) and \
                path[-1] != 'end' and el != 'start':
            temp1.append(el)

        if temp1 != path or temp1[-1] == 'end':
            ans.append(temp1)
    return ans


def run(input_list, part2=False):
    temp = initial(input_list)
    next_step = [['start']]
    prev_step = []
    while len(prev_step) != len(next_step):
        prev_step = next_step
        temp4 = []
        for item in next_step:
            temp4.extend(step(item, temp, part2))
        next_step = [list(item) for item in set(tuple(row) for row in temp4)]
    counter = 0

    for item in [list(item) for item in set(tuple(row) for row in next_step)]:
        if item[-1] == 'end':
            counter += 1

    print(counter)


if __name__ == '__main__':
    run(ind)
    run(ind, True)
