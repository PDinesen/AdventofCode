ind = [line.rstrip("\n") for line in open('test2.txt')]


def initialize(ind):
    enhancement = ind[0]
    image = set()
    temp = ind[2:]
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == '#':
                image.add((i, j))
    return enhancement, image


def step(enhancement, image):
    minx, miny = min(x for x, _ in image), min(y for _, y in image)
    maxx, maxy = max(x for x, _ in image), max(y for _, y in image)
    new_image = set()
    for x in range(minx - 2, maxx + 3):
        for y in range(miny - 2, maxy + 3):
            lookup = ''
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (x + i, y + j) in image:
                        lookup += '1'
                    else:
                        lookup += '0'
            if enhancement[int(lookup, 2)] == '#':
                new_image.add((x, y))
    return new_image


def run(ind, n):
    enhancement, image = initialize(ind)
    for _ in range(n):
        image = step(enhancement, image)
    return image


image = run(ind, 2)
print(len(image))


def print_board(image):
    minx, miny, maxx, maxy = min(x for x, y in image), min(y for x, y in image), max(x for x, _ in image), max(y for _, y in image)

    for i in range(minx, maxx + 1):
        output = ''
        for j in range(miny, maxy + 1):
            if (i, j) in image:
                output += '#'
            else:
                output += '.'
        print(output)


print_board(image)