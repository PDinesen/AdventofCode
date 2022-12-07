def solve(txt_name):
    st = [item.split(' ') for item in [contents.rstrip('\n') for contents in open(txt_name)]]
    make_dict = dict()
    temp = []
    append_it = False
    key = []
    for line in st:
        if len(line) == 3:
            if append_it:
                make_dict[''.join(key)] = temp
            if line[2] == '..':
                key = key[:-1]
            else:
                key.append(line[2])
            append_it = False
        elif line[1] == 'ls':
            temp = []
        else:
            if line[0] == 'dir':
                temp.append(''.join(key) + line[1])
            else:
                temp.append(int(line[0]))
            append_it = True
    if append_it:
        make_dict[''.join(key)] = temp

    def sum_dict(the_key):
        summen = 0
        for item in make_dict[the_key]:
            if isinstance(item, int):
                summen += item
            else:
                summen += sum_dict(item)
        return summen

    for key in make_dict.keys():
        make_dict[key] = sum_dict(key)

    part1 = sum(val for val in make_dict.values() if val <= 100000)
    part2 = min(val for val in make_dict.values() if val >= 30000000 - (70000000 - make_dict['/']))

    print('day 7 part 1: ' + str(part1))
    print('day 7 part 2: ' + str(part2))


if __name__ == '__main__':
    solve('day7.txt')
