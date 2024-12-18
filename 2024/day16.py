import heapq

st = [item for item in [content.rstrip('\n') for content in open('input/' + 'day16' + '.txt')]]


def find_pos(grid: list[str], start_end):
    for row in range(len(grid)):
        if start_end in grid[row]:
            return row, grid[row].index(start_end)
    return None


def print_track(grid, seats):
    for row in range(len(grid)):
        l = ''
        for col in range(len(grid[row])):
            if (row, col) in seats:
                l += 'O'
            else:
                l += grid[row][col]
        print(l)


def step(grid, pos_dir, rev=False):
    if rev:
        i = -1
    else:
        i = 1
    ((r, c), (dr, dc)) = pos_dir
    yield 1000, ((r, c), (-dc, dr))
    yield 1000, ((r, c), (dc, -dr))
    if grid[r + i * dr][c + i * dc] != '#':

        yield 1, ((r + i * dr, c + i * dc), (dr, dc))


def djikstra_t(grid, adj_list, nodes, rev=False):
    dists = {}
    heap = []
    for node in nodes:
        heapq.heappush(heap, (0, node))
    while heap:
        dist, u = heapq.heappop(heap)
        if u in dists:
            continue
        dists[u] = dist
        neighbors = adj_list(grid, u, rev)
        for weight, v in neighbors:
            heapq.heappush(heap, (dist + weight, v))
    return dists


def run(grid):
    dist = djikstra_t(grid, step, [(find_pos(grid, 'S'), (0, 1))])
    end_pos = find_pos(grid, 'E')
    target = [(end_pos, d) for d in [(-1, 0), (0, -1), (1, 0), (0, 1)]]
    ans1 = min(dist[t] for t in target)
    print(ans1)

    dist_rev = djikstra_t(grid, step, target, True)
    on = {u for u in dist if dist_rev[u] + dist[u] == ans1}
    best = {pos for pos, _ in on}
    #print_track(grid, best)
    print(len(best))


run(st)


