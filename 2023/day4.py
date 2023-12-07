def solution(txt, part1=True):

    st = [item for item in [contents.rstrip('\n') for contents in open('input/' + txt + '.txt')]]

    result = 0
    cards = []
    copies = [1] * len(st)
    for i, line in enumerate(st):
        card, rest = line.split(':')[0], line.split(':')[1]
        win, mine = list(map(int, rest.split(' | ')[0].split())), list(map(int, rest.split(' | ')[1].split()))
        cards.append((1, card, win, mine))
        res = 0
        tr = 0
        for el in win:
            if el in mine:
                res += 1
                tr = 1
        if part1:
            result += int(tr * 2 ** (res - 1))
        else:
            times = copies[i]
            for j in range(res):
                copies[i + j + 1] += times

    if part1:
        print(result)
    else:
        print(sum(copies))


if __name__ == '__main__':
    solution('day4')
    solution('day4', False)
