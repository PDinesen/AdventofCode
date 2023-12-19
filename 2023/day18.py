def polygonArea(vertices):
    # A function to apply the Shoelace algorithm
    numberOfVertices = len(vertices)
    sum1 = 0
    sum2 = 0

    for i in range(0, numberOfVertices - 1):
        sum1 = sum1 + vertices[i][0] * vertices[i + 1][1]
        sum2 = sum2 + vertices[i][1] * vertices[i + 1][0]

    # Add xn.y1
    sum1 = sum1 + vertices[numberOfVertices - 1][0] * vertices[0][1]
    # Add x1.yn
    sum2 = sum2 + vertices[0][0] * vertices[numberOfVertices - 1][1]

    area = abs(sum1 - sum2) // 2
    return area


st = [tuple(contents.rstrip('\n').split(' ')) for contents in open('input/' + 'day18' + '.txt')]


def edge_range(lst, part1=True):
    s = (0, 0)
    corners = []
    bound = 0
    ways = 'RDLU'
    for w, l, c in lst:
        if part1:
            l = int(l)
        else:
            w = ways[int(c[-2])]
            l = int(c[2:-2], 16)
        if w == 'R':
            s = (s[0], s[1] + l)
        elif w == 'D':
            s = (s[0] + l, s[1])
        elif w == 'L':
            s = (s[0], s[1] - l)
        elif w == 'U':
            s = (s[0] - l, s[1])
        corners.append(s)
        bound += l
    return polygonArea(corners) + bound // 2 + 1

print(edge_range(st))
print(edge_range(st, False))
