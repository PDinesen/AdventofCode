def solve(txt_name):
    st = [item for item in [contents.rstrip('\n') for contents in open(txt_name)]]

    points = ' abcdefghijklmnopqrstuvwxyz'
    points += points[1:].upper()

    total = 0
    for item in st:
        w1 = item[:len(item) // 2]
        w2 = item[len(item) // 2:]
        for letter in w1:
            if letter in w2:
                total += points.index(letter)
                break
    print('day 3 part 1: ' + str(total))

    total2 = 0
    for i in range(0, len(st), 3):
        w1 = ''.join(set(st[i]))
        w2 = ''.join(set(st[i+1]))
        w3 = ''.join(set(st[i+2]))

        p = ''
        for letter in w1:
            if letter in w2 and letter in w3:
                if p == '':
                    p = letter
                else:
                    p = ''
                    break

        if p != '':
            total2 += points.index(p)
    print('day 3 part 2: ' + str(total2))


if __name__ == '__main__':
    solve('day3.txt')
