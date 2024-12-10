st = [item for item in [contents.rstrip('\n') for contents in open('input/' + 'day6' + '.txt')]]

print(st)

for i in range(len(st)):
    if '^' in st[i]:
        print(i, st[i].index('^'))
        start_pos = (i, st[i].index('^'))
        break

visit = set()

visit.add(start_pos)
print(visit)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

d = directions[0]
curr_pos = start_pos
still_here = True
while still_here:
    nr, nc = curr_pos[0] + d[0], curr_pos[1] + d[1]
    if nr < 0 or nr >= len(st) or nc < 0 or nc >= len(st[0]):
        still_here = False
        break
    elif st[nr][nc] == '#':
        d = directions[(directions.index(d) + 1) % len(directions)]
    else:
        visit.add((nr,nc))
        curr_pos = (nr, nc)

print(len(visit))
count = 0
j = 0
for r, c in visit:
    if (r, c) != start_pos:

        d = directions[0]
        pos_direction = [start_pos + d]
        grid = st.copy()
        grid[r] = grid[r][:c] + '#' + grid[r][c+1:]
        d = directions[0]
        curr_pos = start_pos
        still_here = True
        i = 0
        while still_here:
            nr, nc = curr_pos[0] + d[0], curr_pos[1] + d[1]
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                still_here = False
            elif grid[nr][nc] == '#':
                d = directions[(directions.index(d) + 1) % len(directions)]
            elif (nr, nc) + d in pos_direction:
                break
            else:
                curr_pos = (nr, nc)
                pos_direction.append(curr_pos + d)
            i += 1

        if still_here:
            count += 1
    j += 1
    if j % 500 == 0:
        print(j)

print(count)

