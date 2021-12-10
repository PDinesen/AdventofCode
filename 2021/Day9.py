input_list = [line.rstrip('\n') for line in open('input9.txt')]

cd = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def neighbor_pos(position, rows, cols):
    x, y = position
    return [(x + row, y + col) for row, col in cd if 0 <= x + row < rows and 0 <= y + col < cols]


def basin(ind, location):
    locations = {location}
    size = 0
    rows = len(ind)
    cols = len(ind[0])
    while len(locations) != size:
        size = len(locations)
        temp = locations.copy()
        for loc in temp:
            row, col = loc
            for i, j in neighbor_pos(loc, rows, cols):
                if int(ind[row][col]) + 1 <= int(ind[i][j]) < 9:
                    locations.add((i, j))
    return size


def run(ind):
    ans = 0
    low_locations = []
    rows = len(ind)
    cols = len(ind[0])
    for row in range(rows):
        for col in range(cols):
            if all(int(ind[row][col]) < int(ind[i][j]) for i, j in neighbor_pos((row, col), rows, cols)):
                ans += int(ind[row][col]) + 1
                low_locations.append((row, col))
    print(ans)
    sizes = sorted(basin(ind, item) for item in low_locations)
    print(sizes[-1] * sizes[-2] * sizes[-3])


if __name__ == '__main__':
    run(input_list)
