def initialize(filename):
    ind = [line.rstrip("\n") for line in open(filename)]
    enhancement = ind[0]
    image = set()
    temp = ind[2:]
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == '#':
                image.add((i, j))
    return enhancement, image


def step(enhancement, image, even=False):
    min_x, min_y = min(x for x, _ in image), min(y for _, y in image)
    max_x, max_y = max(x for x, _ in image), max(y for _, y in image)
    new_image = set()
    odd_image = enhancement[0]
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            lookup = ''
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if ((x + i) < min_x or (x + i) > max_x or (y + j) < min_y or (y + j) > max_y) and even:
                        if odd_image == '#':
                            lookup += '1'
                        else:
                            lookup += '0'
                    else:
                        if (x + i, y + j) in image:
                            lookup += '1'
                        else:
                            lookup += '0'
            if enhancement[int(lookup, 2)] == '#':
                new_image.add((x, y))
    return new_image


def run(filename, n):
    enhancement, image = initialize(filename)
    for i in range(1, n + 1):
        if i % 2 == 0:
            image = step(enhancement, image, True)
        else:
            image = step(enhancement, image)
    print(len(image))
    return image


def print_board(image):
    min_x, min_y = min(x for x, y in image), min(y for x, y in image)
    max_x, max_y = max(x for x, _ in image), max(y for _, y in image)
    for i in range(min_x, max_x + 1):
        output = ''
        for j in range(min_y, max_y + 1):
            if (i, j) in image:
                output += '#'
            else:
                output += '.'
        print(output)


if __name__ == '__main__':
    run('input20.txt', 2)
    run('input20.txt', 50)
    # print_board(image)
