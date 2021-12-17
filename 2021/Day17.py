def euler(n):
    return n * (1 + n) // 2


def back_euler(n, rounding=None):
    x = (-1 + (1 + 8 * n)**(1/2)) / 2
    if rounding == 'down':
        return int(x)
    elif rounding == 'up':
        if x == int(x):
            return int(x)
        else:
            return int(x) + 1
    return x


def run(input_list):
    return euler(abs(input_list[1][0]) - 1)


def get_x(temp):
    low_x = back_euler(temp[0], 'up')
    xl = []
    for j in range(low_x, temp[1] + 1):
        j_e = euler(j)
        for i in range(j + 1):
            if j_e in range(temp[0], temp[1] + 1):
                xl.append(j)
                break
            else:
                j_e -= i
    return xl


def target(x, y, input_list):
    x_p = y_p = 0
    dx, dy = x, y
    while y_p >= input_list[1][0] and x_p <= input_list[0][1]:
        if x_p in range(input_list[0][0], input_list[0][1] + 1)\
                and y_p in range(input_list[1][0], input_list[1][1] + 1):
            return True
        else:
            x_p += dx
            dx = max(dx - 1, 0)
            y_p += dy
            dy -= 1
    return False


def run2(input_list):
    xl = get_x(input_list[0])
    y_max = abs(input_list[1][0]) - 1
    y_min = input_list[1][0]
    paths = []
    for x in xl:
        for y in range(y_min, y_max + 1):
            if target(x, y, input_list):
                paths.append((x, y))

    return len(paths)


if __name__ == '__main__':
    ind = [line.rstrip('\n') for line in open('input17.txt')]
    ind = [list(map(int, i[2:].split('..'))) for i in ind[0].split(': ')[1].split(', ')]

    print('Part 1: ' + str(run(ind)))
    print('Part 2: ' + str(run2(ind)))
