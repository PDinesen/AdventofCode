import AOCH
from math import cos, sin, radians

input12 = AOCH.ril('input12.txt')


def run(input_list):
    start = [0, 0]
    rad = 0
    for item in input_list:
        if item[0] == 'N':
            start[1] += int(item[1:])
        elif item[0] == 'S':
            start[1] -= int(item[1:])
        elif item[0] == 'E':
            start[0] += int(item[1:])
        elif item[0] == 'W':
            start[0] -= int(item[1:])
        elif item[0] == 'F':
            start[0] += round(cos(rad) * int(item[1:]))
            start[1] += round(sin(rad) * int(item[1:]))
        elif item[0] == 'R':
            rad -= radians(int(item[1:]))
        elif item[0] == 'L':
            rad += radians(int(item[1:]))
    return start


print(run(AOCH.ril('test')))

end_pos = run(input12)
print(abs(end_pos[0]) + abs(end_pos[1]))


def rotate(point, angle):
    px, py = point

    qx = cos(angle) * px - sin(angle) * py
    qy = sin(angle) * px + cos(angle) * py
    return [round(qx), round(qy)]


print(rotate((1, 0), radians(90)))


def run2(input_list, start_waypoint):
    start = [0, 0]
    point = start_waypoint
    for item in input_list:
        if item[0] == 'N':
            point[1] += int(item[1:])
        elif item[0] == 'S':
            point[1] -= int(item[1:])
        elif item[0] == 'E':
            point[0] += int(item[1:])
        elif item[0] == 'W':
            point[0] -= int(item[1:])
        elif item[0] == 'F':
            start[0] += point[0] * int(item[1:])
            start[1] += point[1] * int(item[1:])
        elif item[0] == 'R':
            point = rotate(point, -radians(int(item[1:])))
        elif item[0] == 'L':
            point = rotate(point, radians(int(item[1:])))
        print(start, point)
    return start


print(run2(AOCH.ril('test'), [10, 1]))
end_pos = run2(input12, [10, 1])
print(abs(end_pos[0]) + abs(end_pos[1]))
