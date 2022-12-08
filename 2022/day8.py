def solve(txt_name):
    st = [list(map(int, list(item))) for item in [contents.rstrip('\n') for contents in open(txt_name)]]

    lenght = len(st[0])
    hight = len(st)

    def vert(i, j):
        tree = st[i][j]
        vis_up = True
        vis_down = True
        for k in range(hight):
            if st[k][j] >= tree and k != i:
                if k < i:
                    vis_up = False
                else:
                    vis_down = False
        return vis_up or vis_down

    def hori(i, j):
        tree = st[i][j]
        vis_left = True
        vis_right = True
        for k in range(lenght):
            if st[i][k] >= tree and k != j:
                if k < j:
                    vis_left = False
                else:
                    vis_right = False
        return vis_left or vis_right

    count = 0

    for i_h in range(hight):
        for j_l in range(lenght):
            if vert(i_h, j_l) or hori(i_h, j_l):
                count += 1

    print('day 8 part 1: ' + str(count))

    def find_up(i, j):
        if i == 0:
            return 0
        tree = st[i][j]
        for k in range(i - 1, -1, -1):
            if tree <= st[k][j]:
                return i - k
        return i

    def find_down(i, j):
        if i == hight - 1:
            return 0
        tree = st[i][j]
        for k in range(i + 1, hight):
            if tree <= st[k][j]:
                return k - i
        return hight - 1 - i

    def find_left(i, j):
        if j == 0:
            return 0
        tree = st[i][j]
        for k in range(j - 1, -1, -1):
            if tree <= st[i][k]:
                return j - k
        return j

    def find_right(i, j):
        if j == lenght - 1:
            return 0
        tree = st[i][j]
        for k in range(j + 1, lenght):
            if tree <= st[i][k]:
                return k - j
        return lenght - 1 - j

    save = 0
    for i_h in range(hight):
        for j_l in range(lenght):
            score = find_right(i_h, j_l) * find_left(i_h, j_l) * find_up(i_h, j_l) * find_down(i_h, j_l)
            save = max(save, score)
    print('day 8 part 2: ' + str(save))


if __name__ == '__main__':
    solve('day8.txt')
