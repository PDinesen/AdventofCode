st = [item for item in [contents for contents in open('input/' + 'day4' + '.txt')]]

grid = st
word = 'XMAS'


rows = len(grid)
cols = len(grid)
word_len = len(word)

directions = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)]

count = 0

for r in range(rows):
    for c in range(cols):
        for dr, dc in directions:
            for i in range(word_len):
                nr, nc = r + dr * i, c + dc * i
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                    break
                if i == word_len - 1:
                    count += 1

count2 = 0

for r in range(1, rows - 1):
    for c in range(1, cols - 1):
        if grid[r][c] == 'A':
            dir1 = grid[r - 1][c - 1] + 'A' + grid[r + 1][c + 1]
            dir2 = grid[r + 1][c - 1] + 'A' + grid[r - 1][c + 1]
            if dir1 in ['MAS', 'SAM'] and dir2 in ['MAS', 'SAM']:
                count2 += 1

print(directions)

print(count2)

print(count)
