def solve(txt_name):
    st = [item for item in [contents.rstrip('\n') for contents in open(txt_name)]][0]

    def find(n):
        for i in range(n, len(st)):
            if len(set(st[i - n:i])) == n:
                return i

    print('day 6 part 1: ' + str(find(4)))
    print('day 6 part 2: ' + str(find(14)))


if __name__ == '__main__':
    solve('day6.txt')
