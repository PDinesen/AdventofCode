def solution(txt):
    st = [list(map(int, item.split()[1::])) for item in [contents.rstrip('\n') for contents in open('input/' + txt +
                                                                                                    '.txt')]]
    st2 = []
    for line in st:
        temp = ''
        for el in list(map(str, line)):
            temp += el
        st2.append(int(temp))

    def find_range(_time, _dist):
        disc = (_time ** 2 - 4 * _dist) ** (1 / 2)
        if (_time - disc) / 2 % 1 == 0.0:
            return int((_time - disc) / 2) + 1, int((_time + disc) / 2) - 1
        else:
            return int((_time - disc) / 2) + 1, int((_time + disc) / 2)

    st = list(zip(st[0], st[1]))

    prod = 1
    for time, dist in st:
        start, end = find_range(time, dist)
        prod = prod * (end - start + 1)

    print(prod)

    time = st2[0]
    dist = st2[1]
    start, end = find_range(time, dist)

    print(end - start + 1)


if __name__ == '__main__':
    solution('day6')
