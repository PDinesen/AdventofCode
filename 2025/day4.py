st = [item for item in [content.rstrip('\n') for content in open('day4.txt')]]

def numberOfNeigbohrs(grip, row, col):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (1, 1), (-1, 1), (-1, -1)]
    naboer = 0
    for i, j in directions:
        if 0 <= row + i < len(grip) and 0 <= col + j < len(grip[0]):
            if grip[row + i][col + j] == '@':
                naboer += 1
    return naboer

def removePaper(grid: list[str], places):
    temp = grid.copy()
    for row, col in places:
        temp[row] = temp[row][:col] + "." + temp[row][col + 1:]
    
    return temp

def done(grid):
    for row in grid:
        if '@' in row:
            return False
    return True

def run(grid: list[str]):
    count = 0
    temp = []
    while not done(grid) and temp != grid:
        temp = grid.copy()
        places = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '@':
                    if numberOfNeigbohrs(grid, r, c) < 4:
                        places.append((r, c))
        count += len(places)
        grid = removePaper(grid, places)
    return count


print(run(st, 4))
