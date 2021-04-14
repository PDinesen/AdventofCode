filename = 'input3.txt'

data = [Line.rstrip('\n').split(',') for Line in open(filename)]


def run(input_list):
    points = []
    for line in input_list:
        x, y = (0, 0)
        temp = [[x, y]]
        for item in line:
            if item[0] == 'U':
                x += int(item[1:])
            elif item[0] == 'D':
                x -= int(item[1:])
            elif item[0] == 'R':
                y += int(item[1:])
            elif item[0] == 'L':
                y -= int(item[1:])
            temp.append([x, y])
        points.append(temp)

    intersects = []
    for i in range(len(points[0])-1):
        for j in range(len(points[1])-1):
            if min(points[0][i][0], points[0][i+1][0]) < points[1][j][0] < max(points[0][i][0], points[0][i+1][0]) and \
                    min(points[1][j][1], points[1][j+1][1]) < points[0][i][1] < max(points[1][j][1], points[1][j+1][1]):
                intersects.append([points[1][j][0], points[0][i][1]])
            elif min(points[0][i][1], points[0][i+1][1]) < points[1][j][1] < max(points[0][i][1], points[0][i+1][1]) and \
                    min(points[1][j][0], points[1][j+1][0]) < points[0][i][0] < max(points[1][j][0], points[1][j+1][0]):
                intersects.append([points[0][i][0], points[1][j][1]])
    manhatten = 0
    for point in intersects:
        dist = sum(list(map(abs, point)))
        if dist < manhatten or manhatten == 0:
            manhatten = dist
    min_steps = 0
    for intersection in intersects:
        steps = 0
        for line in points:
            for i in range(len(line)-1):
                if min(line[i][0], line[i+1][0]) < intersection[0] < max(line[i][0], line[i+1][0]) and \
                        line[i][1] == intersection[1]:
                    steps += abs(line[i][0] - intersection[0])
                    break
                elif min(line[i][1], line[i+1][1]) < intersection[1] < max(line[i][1], line[i+1][1]) and \
                        line[i][0] == intersection[0]:
                    steps += abs(line[i][1] - intersection[1])
                    break
                else:
                    steps += abs(line[i][0] - line[i+1][0] + line[i][1] - line[i+1][1])
        if steps < min_steps or min_steps == 0:
            min_steps = steps

    print(min_steps)
    print(manhatten)
    return 0


run(data)
