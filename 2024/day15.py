st = [item for item in [content.rstrip('\n') for content in open('input/' + 'day15' + '.txt')]]


def find_start(house):
    start_pos = (0, 0)
    for r in range(len(house)):
        if '@' in house[r]:
            start_pos = (r, house[r].index('@'))
            break
    return start_pos


def initialize(st_list: list[str], part1=True):
    warehouse = []
    moves = ''
    h = True
    for line in st_list:
        if line == '':
            h = False
        if h:
            line_split = []
            if not part1:
                line = line.replace('#', '##')
                line = line.replace('O', '[]')
                line = line.replace('.', '..')
                line = line.replace('@', '@.')
            for c in line:
                line_split.append(c)
            warehouse.append(line_split)
        else:
            moves += line
    pos = find_start(warehouse)
    return warehouse, moves, pos


direction_map = {'<': (0, -1), '^': (-1, 0), '>': (0, 1), 'v': (1, 0)}


def make_move(house, pos, move, part1=True):
    x, y = pos
    dx, dy = direction_map[move]
    i = 1
    if part1:
        possible = False
        while not possible:
            if house[x + i * dx][y + i * dy] == '.':
                possible = True
                break
            elif house[x + i * dx][y + i * dy] == '#':
                break
            i += 1

        if possible:
            for j in range(i, 0, -1):
                house[x + j * dx][y + j * dy] = house[x + (j - 1) * dx][y + (j - 1) * dy]
            house[x][y] = '.'
            x += dx
            y += dy
    else:
        possible = True
        check_place = {(x, y)}
        checked = []
        while len(check_place) > 0 and possible:
            temp_check_places = set()
            while len(check_place) > 0:
                cx, cy = check_place.pop()
                checked.append((cx, cy))
                if house[cx+dx][cy+dy] == '#':
                    possible = False
                    break
                elif house[cx+dx][cy+dy] == '[':
                    if move in 'v^':
                        temp_check_places.add((cx+dx, cy+dy))
                        temp_check_places.add((cx+dx, cy+dy+1))
                    else:
                        temp_check_places.add((cx + 2 * dx, cy + 2 * dy))
                        checked.append((cx + dx, cy + dy))
                elif house[cx+dx][cy+dy] == ']':
                    if move in 'v^':
                        temp_check_places.add((cx+dx, cy+dy))
                        temp_check_places.add((cx+dx, cy+dy-1))
                    else:
                        temp_check_places.add((cx + 2 * dx, cy + 2 * dy))
                        checked.append((cx + dx, cy + dy))

            check_place = temp_check_places

        if possible:
            for mx, my in checked[::-1]:
                house[mx + dx][my + dy] = house[mx][my]
                if (mx - dx, my - dy) not in checked:
                    house[mx][my] = '.'
            house[x][y] = '.'
            x += dx
            y += dy

    return house, (x, y)


def print_house(house):
    for row in house:
        print("".join(row))


def calc_score(house):
    score = 0

    for row in range(len(house)):
        for col in range(len(house[row])):
            if house[row][col] in 'O[':
                score += 100 * row + col

    print(score)


def run(st_list, part1=True):
    house, moves, start = initialize(st_list, part1)
    for m in moves:
        house, start = make_move(house, start, m, part1)

    calc_score(house)


run(st)
run(st, False)
