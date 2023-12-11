st = [contents.rstrip('\n') for contents in open('input/' + 'day10' + '.txt')]

move = {'down': {'|': 'down', 'L': 'right', 'J': 'left'},
        'up': {'|': 'up', '7': 'left', 'F': 'right'},
        'left': {'-': 'left', 'L': 'up', 'F': 'down'},
        'right': {'-': 'right', 'J': 'up', '7': 'down'}}


def find_start(lst):
    for i, line in enumerate(lst):
        if 'S' in line:
            return i, line.index('S')


s0, s1 = find_start(st)

been = [(s0, s1)]
ways = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def check_neigbors(p0, p1, direction):
    if direction == 'up':
        if st[p0 - 1][p1] == 'S':
            return p0 - 1, p1, 'stop'
        return p0 - 1, p1, move[direction][st[p0 - 1][p1]]
    elif direction == 'down':
        if st[p0 + 1][p1] == 'S':
            return p0 + 1, p1, 'stop'
        return p0 + 1, p1, move[direction][st[p0 + 1][p1]]
    elif direction == 'right':
        if st[p0][p1 + 1] == 'S':
            return p0, p1 + 1, 'stop'
        return p0, p1 + 1, move[direction][st[p0][p1 + 1]]
    elif direction == 'left':
        if st[p0][p1 - 1] == 'S':
            return p0, p1 - 1, 'stop'
        return p0, p1 - 1, move[direction][st[p0][p1 - 1]]


def get_start(lst):
    p0, p1 = find_start(lst)
    directions = []
    if p0 + 1 < len(lst) and lst[p0 + 1][p1] in move['down']:
        directions.append('down')
    if p0 - 1 >= 0 and lst[p0 - 1][p1] in move['up']:
        directions.append('up')
    if p1 + 1 < len(lst[0]) and lst[p0][p1 + 1] in move['right']:
        directions.append('right')
    if p1 - 1 >= 0 and lst[p0][p1 - 1] in move['left']:
        directions.append('left')
    return p0, p1, directions[0], directions[1]


s0, s1, dire, dire2 = get_start(st)



positions = []
while dire != 'stop':
    positions.append([s0, s1])
    s0, s1, dire = check_neigbors(s0, s1, dire)

if dire == 'down' and dire2 == 'up':
    st[s0] = st[s0].replace('S', '|')
elif dire == 'down' and dire2 == 'right':
    st[s0] = st[s0].replace('S', 'F')
elif dire == 'down' and dire2 == 'left':
    st[s0] = st[s0].replace('S', '7')
elif dire == 'up' and dire2 == 'right':
    st[s0] = st[s0].replace('S', 'L')
elif dire == 'up' and dire2 == 'left':
    st[s0] = st[s0].replace('S', 'J')
elif dire == 'right' and dire2 == 'left':
    st[s0] = st[s0].replace('S', '-')

inder = 0
save = []
last = '.'
for i in range(len(st)):
    count = 0
    for j in range(1, len(st[0])):
        if [i, j] in positions:
            if st[i][j] in 'LF':
                last = st[i][j]
            elif st[i][j] == '7':
                if last == 'L':
                    count += 1
            elif st[i][j] == 'J':
                if last == 'F':
                    count += 1
            elif st[i][j] == '|':
                count += 1

        elif count % 2 == 1 and [i, j] not in positions:
            save.append([i, j])
            inder += 1

print(inder)
print(save)


