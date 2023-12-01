def solve(txt, task2=False):
    st = [item for item in [contents.rstrip('\n') for contents in open('input/' + txt)]]

    res = 0
    test = [str(i) for i in range(10)]
    if task2:
        test = [' ', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] + test
    for word in st:
        low = (len(word), -1)
        high = (-1, -1)
        for i, tjek in enumerate(test):
            if tjek in word:
                if word.index(tjek) < low[0]:
                    low = (word.index(tjek), int(str(i)[-1]))
                if word.rindex(tjek) > high[0]:
                    high = (word.rindex(tjek), int(str(i)[-1]))

        res += low[1] * 10 + high[1]

    return res


if __name__ == '__main__':
    print('Solution task1: ' + str(solve('day1.txt')))
    print('Solution task2: ' + str(solve('day1.txt', True)))
