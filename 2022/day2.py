def solve(txt_name):
    st = [item for item in [contents.rstrip('\n') for contents in open(txt_name)]]

    p1_hand = ['A', 'B', 'C']
    p2_hand = ['X', 'Y', 'Z']

    task_1 = 0
    for item in st:
        if p1_hand.index(item[0]) == p2_hand.index(item[2]):
            task_1 += p2_hand.index(item[2]) + 4
        elif p1_hand.index(item[0]) == (p2_hand.index(item[2]) - 1) % 3:
            task_1 += p2_hand.index(item[2]) + 7
        else:
            task_1 += p2_hand.index(item[2]) + 1
    print(task_1)

    task_2 = 0
    for item in st:
        if item[2] == 'X':
            task_2 += 1 + (p1_hand.index(item[0]) - 1) % 3
        elif item[2] == 'Y':
            task_2 += 4 + p1_hand.index(item[0])
        else:
            task_2 += 7 + (p1_hand.index(item[0]) + 1) % 3
    print(task_2)


if __name__ == '__main__':
    solve('day2.txt')

    res1 = 13009
    res2 = 10398
