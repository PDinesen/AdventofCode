def solve(txt_name):
    st = [list(item) for item in [contents.rstrip('\n') for contents in open(txt_name)]]

    width = len(st[0])
    height = len(st)
    start_pos = None
    end_pos = None
    num = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(height):
        for j in range(width):
            if st[i][j] == 'S':
                start_pos = (i, j)
                st[i][j] = 0
            elif st[i][j] == 'E':
                end_pos = (i, j)
                st[i][j] = num.index('z')
            else:
                st[i][j] = num.index(st[i][j])

    inf = 10000

    class Node:
        def __init__(self):
            self.name = '.'
            self.neighbors = []
            self.dist = inf
            self.seen = False

    verts = [Node() for _ in range(width * height)]
    targets = []
    source = None

    for i, r in enumerate(st):
        for j, c in enumerate(r):
            v = verts[(width * i) + j]
            if (i, j) == start_pos:
                v.name = 'S'
            else:
                v.name = str(c)
            if c == 0:
                targets.append(v)
            elif (i, j) == end_pos:
                source = v
            if i < (height - 1) and c <= st[i + 1][j] + 1:
                v.neighbors.append(width * (i + 1) + j)
            if j < (width - 1) and c <= st[i][j + 1] + 1:
                v.neighbors.append(width * i + j + 1)
            if i > 0 and c <= st[i - 1][j] + 1:
                v.neighbors.append(width * (i - 1) + j)
            if j > 0 and c <= st[i][j - 1] + 1:
                v.neighbors.append((width * i) + j - 1)

    def pop_min_dist(q):
        m = inf
        best_idx = 0
        for idx, node in enumerate(q):
            if node.dist < m:
                m = node.dist
                best_idx = idx
        return q.pop(best_idx)

    def dijkstra(nodes, end):
        q = []
        for node in nodes:
            q.append(node)
        end.dist = 0

        while len(q) > 0:
            u = pop_min_dist(q)
            u._seen = True
            for vi in u.neighbors:
                node = nodes[vi]
                if not node.seen:
                    alt = u.dist + 1  # Graph distance is always 1
                    if alt < node.dist:
                        node.dist = alt
                        node.prev = u

    dijkstra(verts, source)
    part1 = None
    part2 = targets[0]
    for v in targets:
        if v.dist < part2.dist:
            part2 = v
        if v.name == "S":
            part1 = v
    print('Day 12 part 1: ' + str(part1.dist))
    print('Day 12 part 2: ' + str(part2.dist))


if __name__ == '__main__':
    solve('day12.txt')
