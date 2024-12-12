import time
st = [item for item in [content.rstrip('\n') for content in open('input/' + 'day12' + '.txt')]]

t0 = time.time()
hole_grid = [(x, y) for x in range(len(st)) for y in range(len(st[0]))]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def find_round(grid, position, rest):
    r, c = position
    n = []
    f = 4
    f_direction = []
    for dr, dc in directions:
        if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]) and grid[r + dr][c + dc] == grid[r][c]:
            f -= 1
            if (r + dr, c + dc) in rest:
                n.append((r + dr, c + dc))
        else:
            f_direction.append(((r, c), (dr, dc)))
    return n, f, f_direction

res = 0
res2 = 0
while len(hole_grid) > 0:
    fence_direction = []
    same_garden = 1
    fence = 0
    r, c = hole_grid.pop()
    garden_type = st[r][c]
    q, df, dfd = find_round(st, (r, c), hole_grid)
    fence += df
    for el in dfd:
        fence_direction.append(el)
    for rr, rc in q:
        hole_grid.remove((rr, rc))
    while len(q) > 0:
        nr, nc = q.pop()
        same_garden += 1
        q_add, df, dfd = find_round(st, (nr, nc), hole_grid)
        fence += df
        for el in dfd:
            fence_direction.append(el)
        for rr, rc in q_add:
            hole_grid.remove((rr, rc))
            q.append((rr, rc))
    res += same_garden * fence
    sides = 0
    while len(fence_direction) > 0:
        pos, direc = fence_direction.pop()
        sides += 1
        if direc[0] == 0:
            for dr in [-1, 1]:
                nex = True
                new_pos = pos
                while nex:
                    if ((new_pos[0] + dr, new_pos[1]), direc) in fence_direction:
                        fence_direction.remove(((new_pos[0] + dr, new_pos[1]), direc))
                        new_pos = (new_pos[0] + dr, new_pos[1])
                    else:
                        nex = False
        else:
            for dc in [-1, 1]:
                nex = True
                new_pos = pos
                while nex:
                    if ((new_pos[0], new_pos[1] + dc), direc) in fence_direction:
                        fence_direction.remove(((new_pos[0], new_pos[1] + dc), direc))
                        new_pos = (new_pos[0], new_pos[1] + dc)
                    else:
                        nex = False
    res2 += sides * same_garden

print(res)
print(res2)
print(time.time() - t0)