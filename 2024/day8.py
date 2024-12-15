st = [item for item in [contents.rstrip('\n') for contents in open('input/' + 'day8' + '.txt')]]

d = dict()
rows = len(st)
cols = len(st[0])
for r in range(rows):
    for c in range(cols):
        if st[r][c] != '.':
            if st[r][c] in d.keys():
                d[st[r][c]].append((r, c))
            else:
                d[st[r][c]] = [(r, c)]

anti = set()
for k in d.keys():
    for i in range(len(d[k]) - 1):
        for j in range(i + 1, len(d[k])):
            dr, dc = d[k][i][0] - d[k][j][0], d[k][i][1] - d[k][j][1]
            if 0 <= d[k][i][0] + dr < rows and 0 <= d[k][i][1] + dc < cols:
                anti.add((d[k][i][0] + dr, d[k][i][1] + dc))
            if 0 <= d[k][j][0] - dr < rows and 0 <= d[k][j][1] - dc < cols:
                anti.add((d[k][j][0] - dr, d[k][j][1] - dc))

print(len(anti))

anti2 = set()
for k in d.keys():
    for i in range(len(d[k]) - 1):
        for j in range(i + 1, len(d[k])):
            dr, dc = d[k][i][0] - d[k][j][0], d[k][i][1] - d[k][j][1]
            inside = True
            t = 0
            while inside:
                if 0 <= d[k][i][0] + t * dr < rows and 0 <= d[k][i][1] + t * dc < cols:
                    anti2.add((d[k][i][0] + t * dr, d[k][i][1] + t * dc))
                    t += 1
                else:
                    inside = False
            inside = True
            t = 0
            while inside:
                if 0 <= d[k][j][0] - t * dr < rows and 0 <= d[k][j][1] - t * dc < cols:
                    anti2.add((d[k][j][0] - t * dr, d[k][j][1] - t * dc))
                    t += 1
                else:
                    inside = False


print(len(anti2))
