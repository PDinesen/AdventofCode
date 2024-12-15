st = [item.split(' ') for item in [content.rstrip('\n') for content in open('input/' + 'day14' + '.txt')]]
robots = []

cols = 11

for line in st:
    pos = list(map(int, line[0].split('=')[1].split(',')))
    vel = list(map(int, line[1].split('=')[1].split(',')))
    robots.append((pos, vel))


def move(all_robots, wide, tall, seconds):
    new_positions = []
    for robot in all_robots:
        x, y = robot[0]
        dx, dy = robot[1]
        new_positions.append(((x + dx * seconds) % wide, (y + dy * seconds) % tall))

    return new_positions


def print_bathroom(positions: list[tuple[int, int]], wide, tall):
    for r in range(tall):
        row = ''
        for c in range(wide):
            if (c, r) not in positions:
                row += '.'
            else:
                row += str(positions.count((c, r)))
        print(row)


def count_q(positions: list[tuple[int, int]], wide, tall):
    quads = [0] * 4
    for x, y in positions:
        if x < wide // 2 and y < tall // 2:
            quads[0] += 1
        elif x < wide // 2 and y >= tall - tall // 2:
            quads[1] += 1
        elif x >= wide - wide // 2 and y < tall // 2:
            quads[2] += 1
        elif x >= wide - wide // 2 and y >= tall - tall // 2:
            quads[3] += 1

    return quads


def run(all_robots, wide, tall, second):
    positions = move(all_robots, wide, tall, second)
    quadrants = count_q(positions, wide, tall)
    p = 1
    for el in quadrants:
        p *= el
    print(p, quadrants)


def find_top(positions, rows):
    for x, y in positions:
        found = True
        for r in range(1, rows):
            for c in range(-rows, rows + 1):
                if (x + r, y + c) not in positions:
                    found = False
                    break
            if not found:
                break
        if found:
            return True
    return False


run(robots, 101, 103, 100)

for i in range(10000):
    robot_positions = move(robots, 101, 103, i)
    if find_top(robot_positions, 5):
        print_bathroom(robot_positions, 101, 103)
        break
