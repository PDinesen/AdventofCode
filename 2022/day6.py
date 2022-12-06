def solve(txt_name):
    st = [item for item in [contents.rstrip('\n') for contents in open(txt_name)]]
    st = st[0]

    for i in range(3, len(st)):
        if len(set(st[i - 4:i])) == 4:
            print('day 6 part 1: ' + str(i))
            print(st[i - 4:i])
            break

    for i in range(13, len(st)):
        if len(set(st[i - 14:i])) == 14:
            print('day 6 part 2: ' + str(i))
            print(st[i - 14:i])
            break


if __name__ == '__main__':
    solve('day6.txt')
