st = [item for item in [contents.rstrip('\n') for contents in open('input/' + 'day10' + '.txt')]]

directions = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != y and (x == 0 or y == 0) ]
print(st)

print(directions)


def find_zero(grip):
    pos = []
    for r in range(len(grip)):
        for c in range(len(grip[r])):
            if grip[r][c] == '0':
                pos.append((r, c))
    return pos


def find_next(grip, height, sp, cp, trail, count = 0):
    if height == 9:
        trail.add(sp + cp)
        return trail, count + 1
    pos = []
    x, y = cp
    for dr, dc in directions:
        if 0 <= x + dr < len(grip) and 0 <= y + dc < len(grip[0]) and grip[x + dr][y + dc] == str(height + 1):
            pos.append((x + dr, y + dc))
    for current in pos:
        trail, count = find_next(grip, height + 1, sp, current, trail, count)
    return trail, count


def run(grip):
    pos = find_zero(grip)
    count = 0
    trails = set()
    for current in pos:
        trails, c = find_next(grip, 0, current, current, trails)
        count += c
    print(count)
    print(len(trails))

run(st)