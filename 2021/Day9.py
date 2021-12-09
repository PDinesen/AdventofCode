from functools import reduce

input_list = [line.rstrip('\n') for line in open('input9.txt')]

sum_ans = 0
low_locations = []
for i in range(len(input_list)):
    for j in range(len(input_list[0])):
        print(i, j)
        if i + j == 0:
            if int(input_list[i][j]) < int(input_list[i + 1][j]) \
                    and int(input_list[i][j]) < int(input_list[i][j + 1]):
                sum_ans += int(input_list[i][j]) + 1
                low_locations.append((i, j))
        elif i == 0:
            if j == len(input_list[0]) - 1:
                if int(input_list[i][j]) < int(input_list[i + 1][j]) \
                        and int(input_list[i][j]) < int(input_list[i][j - 1]):
                    sum_ans += int(input_list[i][j]) + 1
                    low_locations.append((i, j))
            else:
                if int(input_list[i][j]) < int(input_list[i + 1][j]) \
                        and int(input_list[i][j]) < int(input_list[i][j + 1]) \
                        and int(input_list[i][j]) < int(input_list[i][j - 1]):
                    sum_ans += int(input_list[i][j]) + 1
                    low_locations.append((i, j))
        elif j == 0:
            if i == len(input_list) - 1:
                if int(input_list[i][j]) < int(input_list[i][j + 1]) \
                        and int(input_list[i][j]) < int(input_list[i - 1][j]):
                    sum_ans += int(input_list[i][j]) + 1
                    low_locations.append((i, j))
            else:
                if int(input_list[i][j]) < int(input_list[i + 1][j]) \
                        and int(input_list[i][j]) < int(input_list[i - 1][j]) \
                        and int(input_list[i][j]) < int(input_list[i][j + 1]):
                    sum_ans += int(input_list[i][j]) + 1
                    low_locations.append((i, j))
        elif i + j == len(input_list) + len(input_list[0]) - 2:
            if int(input_list[i][j]) < int(input_list[i - 1][j]) \
                    and int(input_list[i][j]) < int(input_list[i][j - 1]):
                sum_ans += int(input_list[i][j]) + 1
                low_locations.append((i, j))
        elif i == len(input_list) - 1:
            if int(input_list[i][j]) < int(input_list[i - 1][j]) \
                    and int(input_list[i][j]) < int(input_list[i][j + 1]) \
                    and int(input_list[i][j]) < int(
                    input_list[i][j - 1]):
                sum_ans += int(input_list[i][j]) + 1
                low_locations.append((i, j))
        elif j == len(input_list[0]) - 1:
            if int(input_list[i][j]) < int(input_list[i + 1][j]) \
                    and int(input_list[i][j]) < int(input_list[i - 1][j]) \
                    and int(input_list[i][j]) < int(
                    input_list[i][j - 1]):
                sum_ans += int(input_list[i][j]) + 1
                low_locations.append((i, j))
        else:
            if int(input_list[i][j]) < int(input_list[i + 1][j]) \
                    and int(input_list[i][j]) < int(input_list[i - 1][j]) \
                    and int(input_list[i][j]) < int(input_list[i][j - 1]) \
                    and int(input_list[i][j]) < int(input_list[i][j + 1]):
                sum_ans += int(input_list[i][j]) + 1
                low_locations.append((i, j))
print(sum_ans)

print(low_locations)


def basin(ind, location):
    locations = {location}
    size = 0
    while len(locations) != size:
        size = len(locations)
        temp = locations.copy()
        for loc in temp:
            row, col = loc
            if row + col == 0:
                if int(ind[row][col]) + 1 <= int(ind[row + 1][col]) < 9:
                    locations.add((row + 1, col))
                if int(ind[row][col]) + 1 <= int(ind[row][col + 1]) < 9:
                    locations.add((row, col + 1))
            elif row == 0:
                if col == len(ind[0]) - 1:
                    if int(ind[row][col]) + 1 <= int(ind[row + 1][col]) < 9:
                        locations.add((row + 1, col))
                    if int(ind[row][col]) + 1 <= int(ind[row][col - 1]) < 9:
                        locations.add((row, col - 1))
                else:
                    if int(ind[row][col]) + 1 <= int(ind[row + 1][col]) < 9:
                        locations.add((row + 1, col))
                    if int(ind[row][col]) + 1 <= int(ind[row][col + 1]) < 9:
                        locations.add((row, col + 1))
                    if int(ind[row][col]) + 1 <= int(ind[row][col - 1]) < 9:
                        locations.add((row, col - 1))
            elif col == 0:
                if row == len(ind) - 1:
                    if int(ind[row][col]) + 1 <= int(ind[row][col + 1]) < 9:
                        locations.add((row, col + 1))
                    if int(ind[row][col]) + 1 <= int(ind[row - 1][col]) < 9:
                        locations.add((row - 1, col))
                else:
                    if int(ind[row][col]) + 1 <= int(ind[row + 1][col]) < 9:
                        locations.add((row + 1, col))
                    if int(ind[row][col]) + 1 <= int(ind[row - 1][col]) < 9:
                        locations.add((row - 1, col))
                    if int(ind[row][col]) + 1 <= int(ind[row][col + 1]) < 9:
                        locations.add((row, col + 1))
            elif row + col == len(ind) + len(ind[0]) - 2:
                if int(ind[row][col]) + 1 <= int(ind[row - 1][col]) < 9:
                    locations.add((row - 1, col))
                if int(ind[row][col]) + 1 <= int(ind[row][col - 1]) < 9:
                    locations.add((row, col - 1))
            elif row == len(ind) - 1:
                if int(ind[row][col]) + 1 <= int(ind[row - 1][col]) < 9:
                    locations.add((row - 1, col))
                if int(ind[row][col]) + 1 <= int(ind[row][col + 1]) < 9:
                    locations.add((row, col + 1))
                if int(ind[row][col]) + 1 <= int(ind[row][col - 1]) < 9:
                    locations.add((row, col - 1))
            elif col == len(ind[0]) - 1:
                if int(ind[row][col]) + 1 <= int(ind[row + 1][col]) < 9:
                    locations.add((row + 1, col))
                if int(ind[row][col]) + 1 <= int(ind[row - 1][col]) < 9:
                    locations.add((row - 1, col))
                if int(ind[row][col]) + 1 <= int(ind[row][col - 1]) < 9:
                    locations.add((row, col - 1))
            else:
                if int(ind[row][col]) + 1 <= int(ind[row + 1][col]) < 9:
                    locations.add((row + 1, col))
                if int(ind[row][col]) + 1 <= int(ind[row - 1][col]) < 9:
                    locations.add((row - 1, col))
                if int(ind[row][col]) + 1 <= int(ind[row][col - 1]) < 9:
                    locations.add((row, col - 1))
                if int(ind[row][col]) + 1 <= int(ind[row][col + 1]) < 9:
                    locations.add((row, col + 1))
    return size


sizes = []
for item in low_locations:
    sizes.append(basin(input_list, item))


print(reduce((lambda x, y: x * y), [sizes.pop(sizes.index(max(sizes))) for _ in range(3)]))
