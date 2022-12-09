def solve(txt_name):
    st = [[item.split(' ')[0], int(item.split(' ')[1])]
          for item in [contents.rstrip('\n') for contents in open(txt_name)]]

    class Rope:
        def __init__(self, name, tail=False):
            self.name = name
            self.tail = tail
            if tail:
                self.tail = Rope(tail)
            self.x = None
            self.y = None
            self.setcoord(0, 0)
            self.vis = {'[0, 0]'}

        def move(self, direction):
            if direction == 'R':
                self.x += 1
            elif direction == 'L':
                self.x -= 1
            elif direction == 'U':
                self.y += 1
            elif direction == 'D':
                self.y -= 1
            if self.tail:
                if abs(self.tail.x - self.x) > 1 and abs(self.tail.y - self.y) > 1:
                    if self.tail.x < self.x:
                        self.get_tail().setcoord(self.get_tail().x + 1, self.get_tail().y)
                    else:
                        self.get_tail().setcoord(self.get_tail().x - 1, self.get_tail().y)
                    if self.tail.y < self.y:
                        self.tail.move('U')
                    else:
                        self.tail.move('D')
                if abs(self.tail.x - self.x) > 1:
                    self.get_tail().setcoord(self.get_tail().x, self.y)
                    if self.tail.x < self.x:
                        self.tail.move('R')
                    else:
                        self.tail.move('L')
                elif abs(self.tail.y - self.y) > 1:
                    self.get_tail().setcoord(self.x, self.get_tail().y)
                    if self.tail.y < self.y:
                        self.tail.move('U')
                    else:
                        self.tail.move('D')

            self.vis.add(str([self.x, self.y]))

        def move_more(self, direction, times):
            for _ in range(times):
                self.move(direction)

        def setcoord(self, x, y):
            self.x = x
            self.y = y

        def set_tail(self, name):
            self.tail = Rope(name)

        def get_tail(self):
            return self.tail

        def get_lengt_vis(self):
            return len(self.vis)

    main_knot = Rope('H')
    cur_knot = main_knot
    for i in range(1, 10):
        cur_knot.set_tail(str(i))
        cur_knot = cur_knot.get_tail()

    for move in st:
        main_knot.move_more(move[0], move[1])

    print('day 9 part 1: ' + str(main_knot.get_tail().get_lengt_vis()))
    print('day 9 part 2: ' + str(cur_knot.get_lengt_vis()))


if __name__ == '__main__':
    solve('day9.txt')
