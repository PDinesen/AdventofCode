def solve(txt_name):
    st = [item.split(' ') for item in [contents.rstrip('\n') for contents in open(txt_name)]]

    x = 1
    cycle = [x]
    for item in st:
        if item[0] == 'noop':
            cycle.append(x)
        else:
            for _ in range(2):
                cycle.append(x)
            x += int(item[1])

    strength = [20, 60, 100, 140, 180, 220]
    ans = 0
    for i in strength:
        ans += i * cycle[i]

    print('day 10 part 1: ' + str(ans))
    temp = ''
    ans_string = []
    for i in range(1, len(cycle)):
        if abs(cycle[i] - ((i - 1) % 40)) <= 1:
            temp += '#'
        else:
            temp += '.'
        if i % 40 == 0:
            ans_string.append(temp)
            temp = ''

    for i in ans_string:
        print(i)
    print('day 10 part 2: ' + 'ERCREPCJ')


if __name__ == '__main__':
    solve('day10.txt')
