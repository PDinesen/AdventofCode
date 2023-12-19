import heapq
from collections import defaultdict


def parse_input(txt_file):
    return [list(map(int, line)) for line in[contents.rstrip('\n') for contents in open('input/' + txt_file + '.txt')]]


def check_part_one(curr_dr, curr_dc, dr, dc, straight):
    if (dr, dc) == (-curr_dr, -curr_dc):
        return None
    if (dr, dc) != (curr_dr, curr_dc):
        return 1
    if (dr, dc) == (curr_dr, curr_dc):
        return straight + 1

def check_part_two(curr_dr, curr_dc, dr, dc, straight):
    if (dr, dc) == (curr_dr, curr_dc):
        return straight + 1
    if (dr, dc) == (-curr_dr, -curr_dc):
        return None
    if straight >= 4 or (curr_dr, curr_dc) == (0, 0):
        return 1

def dijkstra(grid, start, check_function, max_straight):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    distances = {
        (i, j): defaultdict(lambda: float("inf"))
        for j in range(len(grid[0]))
        for i in range(len(grid))
    }
    queue = [(0, start, (0, 0), 1)]
    while queue:
        current_dist, (x, y), (curr_dr, curr_dc), straight = heapq.heappop(queue)
        for dr, dc in directions:
            new_straight = check_function(curr_dr, curr_dc, dr, dc, straight)
            nx, ny = x + dr, y + dc
            if not new_straight or new_straight == max_straight:
                continue
            if 0 <= nx < rows and 0 <= ny < cols:
                new_dist = current_dist + grid[nx][ny]
                if new_dist < distances[(nx, ny)][(dr, dc, new_straight)]:
                    distances[(nx, ny)][(dr, dc, new_straight)] = new_dist
                    heapq.heappush(queue, (new_dist, (nx, ny), (dr, dc), new_straight))
    return distances

def part1(parsed_data):
    distances = dijkstra(parsed_data, (0, 0), check_part_one, 4)
    return min(distances[(len(parsed_data) - 1, len(parsed_data[0]) - 1)].values())

def part2(parsed_data):
    distances = dijkstra(parsed_data, (0, 0), check_part_two, 11)
    return min(heat_loss for (_, _, forwards), heat_loss in distances[len(parsed_data) - 1, len(parsed_data[0]) - 1].items() if forwards >= 4)

if __name__ == "__main__":
    parsed_data = parse_input('day17')
    answer1 = part1(parsed_data)
    answer2 = part2(parsed_data)
    print(answer1)
    print(answer2)