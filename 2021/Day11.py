ind = [list(map(int, char)) for char in [line.rstrip('\n') for line in open('input11.txt')]]

cd = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def neighbor_pos(position, rows, cols):
    x, y = position
    return [(x + row, y + col) for row, col in cd if 0 <= x + row < rows and 0 <= y + col < cols]


def increase(grid):
    temp = []
    for line in grid:
        temp1 = line.copy()
        for col in range(len(line)):
            temp1[col] += 1
        temp.append(temp1)
    return temp




def flashes(grid):
    zeros = []
    sync = False
    flashes = 0
    rows = len(grid)
    cols = len(grid[0])
    while not all(max(elem) <= 9 for elem in [lines for lines in grid]):
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] > 9:
                    flashes += 1
                    zeros.append((x, y))
                    for i, j in neighbor_pos((x, y), rows, cols):
                        grid[i][j] += 1
        for x, y in zeros:
            grid[x][y] = 0

    return grid, flashes


def step(grid):
    return flashes(increase(grid))


def run(ind, n):
    flash = 0
    for i in range(n):
        ind, f = step(ind)
        flash += f
        if max(max(line) for line in ind) == 0:
            print(i+1)

    print(flash)

run(ind, 100)

def run2(ind):
    i = 0
    while True:
        i += 1
        ind, _ = step(ind)
        if max(max(line) for line in ind) == 0:
            return i

print(run2(ind))