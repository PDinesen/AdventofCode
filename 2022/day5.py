def solve(txt_name):
    st = [item for item in [contents.rstrip('\n') for contents in open(txt_name)]]
    moves = []
    stop = ' 1   2   3   4   5   6   7   8   9 '
    col = [''] * 10
    for item in st:
        if item and item[0] == 'm':
            temp = item.split(' ')
            moves.append(list(map(int, temp[1::2])))

    for i in range(st.index(stop) - 1, -1, -1):
        for j in range(1, len(col)):
            if st[i][(j-1)*4 + 1] != ' ':
                col[j] += st[i][(j-1)*4 + 1]

    col2 = col.copy()

    for move in moves:
        for i in range(move[0]):
            col[move[2]] += col[move[1]][-1]
            col[move[1]] = col[move[1]][:-1]

    ans = ''
    for item in col:
        if item:
            ans += item[-1]
    print(ans)

    for move in moves:
        col2[move[2]] += col2[move[1]][-move[0]:]
        col2[move[1]] = col2[move[1]][:-move[0]]

    ans2 = ''
    for item in col2:
        if item:
            ans2 += item[-1]
    print(ans2)


if __name__ == '__main__':
    solve('day5.txt')
