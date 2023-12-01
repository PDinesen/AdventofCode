def solve(txt_name):
    st = [list(map(int, item[0].split(','))) for item in [contents.split('\n') for contents in open(txt_name)]]

    print(st)

    class Cube:
        def __init__(self, xyz):
            self.x = xyz[0]
            self.y = xyz[1]
            self.z = xyz[2]
            self.neigbors = [item for item in [[self.x, self.y, self.z - 1], [self.x, self.y, self.z + 1],
                                               [self.x, self.y - 1, self.z], [self.x, self.y + 1, self.z],
                                               [self.x - 1, self.y, self.z], [self.x + 1, self.y, self.z]]
                             if item not in st]

        def surface(self):
            return len(self.neigbors)

    cubes = []
    for cube in st:
        cubes.append(Cube(cube))

    ans = 0
    total_neigbors = []
    for cube in cubes:
        print(cube.neigbors)
        total_neigbors += cube.neigbors
        ans += cube.surface()
    print(len(total_neigbors))


    remove_air = 0
    while len(total_neigbors) > 0:
        test = total_neigbors[0]
        if total_neigbors.count(test) > 3:
            remove_air += total_neigbors.count(test)
        print(len(total_neigbors))
        while test in total_neigbors:
            total_neigbors.remove(test)
        print(len(total_neigbors))
    print(ans)
    print(ans - remove_air)
    t = [1, 1, 2]
    t.remove(1)
    print(t)

# mellem 1627 og 2533


if __name__ == '__main__':
    solve('day18.txt')