from queue import PriorityQueue
from sys import maxsize


def neighbor_pos(position, max_rc):
    cd = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    rows, cols = max_rc
    x, y = position
    return [(x + row, y + col) for row, col in cd if 0 <= x + row <= rows and 0 <= y + col <= cols]


def initialize(filename):
    input_lines = [line.rstrip('\n') for line in open(filename)]
    part_1 = {}
    for i in range(len(input_lines[0])):
        for j in range(len(input_lines)):
            part_1[(i, j)] = int(input_lines[j][i])
    end1 = max(part_1)

    part_2 = {}
    for i in range(5):
        for j in range(5):
            for x, y in part_1:
                part_2[(x + (end1[0] + 1) * i, y + (end1[1] + 1) * j)] = (part_1[(x, y)] + i + j - 1) % 9 + 1

    return part_1, part_2


def run(temp):
    end = max(temp)
    s_list = PriorityQueue()
    pos = (0, 0)
    dist = {node: 0 if node == pos else maxsize for node in temp}
    while pos != end:
        neighbors = neighbor_pos(pos, end)
        for position in neighbors:
            if dist[pos] + temp[position] < dist[position]:
                dist[position] = dist[pos] + temp[position]
                s_list.put((dist[position], position))

        if not s_list.empty():
            _, pos = s_list.get()
        else:
            break
    return dist[end]


if __name__ == '__main__':
    part1, part2 = initialize('input15.txt')
    print(run(part1))
    print(run(part2))
