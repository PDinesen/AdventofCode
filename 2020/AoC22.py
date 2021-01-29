import AOCH


def run(filename):
    input_list = AOCH.ril2(filename, '')
    p1 = list(map(int, input_list[0][1:]))
    p2 = list(map(int, input_list[1][1:]))
    while len(p1) > 0 and len(p2) > 0:
        if p1[0] > p2[0]:
            p1.append(p1[0])
            p1.append(p2[0])
        else:
            p2.append(p2[0])
            p2.append(p1[0])
        p1 = p1[1:]
        p2 = p2[1:]
        if len(p1) == 0:
            count = 0
            for i in range(len(p2)):
                count += p2[i] * (len(p2) - i)
            return count
        elif len(p2) == 0:
            count = 0
            for i in range(len(p1)):
                count += p1[i] * (len(p1) - i)
            return count


print(run('input22.txt'))


def game(p1, p2):
    p1_temp = []
    p2_temp = []
    while True:
        if p1 in p1_temp or p2 in p2_temp:
            return True, p1
        else:
            p1_temp.append(p1)
            p2_temp.append(p2)
        if p1[0] <= len(p1) - 1 and p2[0] <= len(p2) - 1:
            p1_winner, _ = game(p1[1:p1[0] + 1], p2[1:p2[0] + 1])
        elif p1[0] < p2[0]:
            p1_winner = False
        else:
            p1_winner = True
        if p1_winner:
            p1.append(p1[0])
            p1.append(p2[0])
        else:
            p2.append(p2[0])
            p2.append(p1[0])
        p1 = p1[1:]
        p2 = p2[1:]
        if len(p1) == 0:
            return False, p2
        elif len(p2) == 0:
            return True, p1


def run2(filename):
    input_list = AOCH.ril2(filename, '')
    p1 = list(map(int, input_list[0][1:]))
    p2 = list(map(int, input_list[1][1:]))
    bol, winner_list = game(p1, p2)
    score = 0
    for i in range(len(winner_list)):
        score += winner_list[i] * (len(winner_list) - i)
    return score


print(run2('input22.txt'))