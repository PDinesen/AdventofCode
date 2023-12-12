st = [line.rstrip('\n') for line in open('input/' + 'day11' + '.txt')]


def transpose(lst):
    trans = []
    for j in range(len(lst[0])):
        temp = ''
        for i in range(len(lst)):
            temp += lst[i][j]
        trans.append(temp)
    return trans


def double_row_column(lst):

    for i in range(2):
        result = []
        for line in lst:
            result.append(line)
            if line.count('#') == 0:
                result.append(line)
        lst = transpose(result)
    return lst


def find_galaxy(lst):
    positions = []
    for i in range(len(lst)):
        for j, el in enumerate(lst[i]):
            if el == '#':
                positions.append([i, j])
    return positions

def shortest_dist(g1, g2):
    return abs(g2[1] - g1[1]) + abs(g2[0] - g1[0])

def solution(lst, expand=True):
    if expand:
        galaxy_map = double_row_column(lst)
    else:
        galaxy_map = lst
    galaxy_positions = find_galaxy(galaxy_map)
    path = 0
    for i, gal1 in enumerate(galaxy_positions):
        if i == len(galaxy_positions):
            break
        for gal2 in galaxy_positions[i + 1:]:
            #print(gal1, gal2, shortest_dist(gal1, gal2))
            path += shortest_dist(gal1, gal2)
        #print(path)

    print(path)
    return path


def solution2(lst, expand):
    galaxy_positions = find_galaxy(lst)
    rows = set(x[0] for x in galaxy_positions)
    cols = set(x[1] for x in galaxy_positions)
    #print(rows,cols)
    path = 0
    for i, g1 in enumerate(galaxy_positions):
        for g2 in galaxy_positions[i + 1: len(galaxy_positions)]:
            #print(g1, g2, min(g1[1], g2[1]), max(g1[1], g2[1]))
            for row in range(g1[0], g2[0]):
                path += 1
                if row not in rows:
                    path += expand
            for col in range(min(g1[1], g2[1]), max(g1[1], g2[1])):
                path += 1
                if col not in cols:
                    path += expand
    #print(path)

    #print(galaxy_positions)

    return path


solution(st)

solution(st, False)

print(solution2(st, 999999))

