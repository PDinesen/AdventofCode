def solution(txt, part1=True):
    if part1:
        possiple = ''.join(str(i) for i in range(2, 10)) + 'TJQKA'
    else:
        possiple = 'J' + ''.join(str(i) for i in range(2, 10)) + 'TQKA'
    sort_order = {i: p for p, i in enumerate(possiple)}

    def sort_sum(_hand):
        su = 0
        for p, s in enumerate(_hand):
            su += sort_order[s] * 10 ** (8 - p * 2)
        return su

    st = [[line[0], int(line[1]), sort_sum(line[0])] for line in [contents.split() for contents in open('input/' +
                                                                                                        txt + '.txt')]]
    hands = ['FIVE', 'FOUR', 'HOUSE', 'THREE', 'PAIRS', 'PAIR', 'HIGH']

    def get_type(_hand, part=True):
        temp = []
        joker = _hand.count('J')
        if part:
            search = possiple
        else:
            search = possiple[1::]
        for pos in search:
            temp.append(_hand.count(pos))
        if part:
            if max(temp) == 5:
                return hands[0]
            elif max(temp) == 4:
                return hands[1]
            elif 2 in temp and 3 in temp:
                return hands[2]
            elif max(temp) == 3:
                return hands[3]
            elif temp.count(2) == 2:
                return hands[4]
            elif temp.count(2) == 1:
                return hands[5]
            else:
                return 'HIGH'
        else:
            if max(temp) + joker == 5:
                return hands[0]
            elif max(temp) + joker == 4:
                return hands[1]
            elif joker == 1 and temp.count(2) == 2 or 3 in temp and 2 in temp:
                return hands[2]
            elif max(temp) + joker == 3:
                return hands[3]
            elif temp.count(2) + joker >= 2:
                return hands[4]
            elif temp.count(2) + joker == 1:
                return hands[5]
            else:
                return hands[6]

    order = dict()
    for item in st:
        typed = get_type(item[0], part1)
        try:
            order[typed].append(item)
        except KeyError:
            order[typed] = [item]

    for key in order:
        order[key].sort(key=lambda x: x[2])

    res = 0
    rank = 1
    for hand in hands[::-1]:
        if hand in order.keys():
            for item in order[hand]:
                res += rank * item[1]
                rank += 1

    print(res)


if __name__ == '__main__':
    solution('day7')
    solution('day7', part1=False)
