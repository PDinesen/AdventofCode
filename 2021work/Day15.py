import heapq
from queue import PriorityQueue
from sys import maxsize
ind = [line.rstrip('\n') for line in open('input15.txt')]
temp = {(i, j): int(x) for i, line in enumerate(ind) for j, x in enumerate(line)}
end = max(temp)
print(end)
new_temp = {}
for i in range(5):
    for j in range(5):
        for item in temp:
            x, y = item
            add_number = temp[item] + i + j
            while add_number > 9:
                add_number -= 9
            new_temp[(x + (end[0] + 1) * i, y + (end[1] + 1) * j)] = add_number

print(max(new_temp))


cd = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def neighbor_pos(position, max_rc):
    rows, cols = max_rc
    x, y = position
    return [(x + row, y + col) for row, col in cd if 0 <= x + row <= rows and 0 <= y + col <= cols]


def make_dictionary(input_dict, pos):
    dists = {}
    heap = []
    heapq.heappush(heap, (0, pos))
    while heap:
        dist, u = heapq.heappop(heap)
        if u not in dists:
            dists[u] = dist
            neighbors = neighbor_pos(u, max(input_dict))
            for v in neighbors:
                heapq.heappush(heap, (dist + input_dict[v], v))
    return dists


print(make_dictionary(temp, (0, 0))[end])
#print(make_dictionary(new_temp, (0, 0))[max(new_temp)])


def find_shortest(grid):
    mx, my = max(grid)
    distance = {node: 0 if node == (0,0) else maxsize for node in grid}
    temp = PriorityQueue()
    x = y = 0

    while not (x == mx and y == my):
        for n, m in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if 0 <= x + n <= mx and 0 <= y + m <= my:
                if distance[(x, y)] + grid[(x + n, y + m)] < distance[(x + n, y + m)]:
                    distance[(x + n, y + m)] = distance[(x, y)] + grid[(x + n, y + m)]
                    temp.put((distance[(x + n, y + m)], (x + n, y + m)))

        if not temp.empty():
            new_element = temp.get()
            x, y = new_element[1]
        else:
            break

    return distance[max(distance)]

print(find_shortest(new_temp))