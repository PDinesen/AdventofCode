def solve(txt_name):
    st = [int(content.split('\n')[0]) for content in open(txt_name)]
    print(st)

    class Grove:
        def __init__(self, value: int, before, after):
            self.value = value
            self.before = before
            self.after = after

        def show(self):
            return self.before.value, self.value, self.after.value

    def add_groves(list_numbers):
        before = Grove(list_numbers[0], None, None)
        groves = [before]
        first = before
        n = first
        for number in list_numbers[1:]:
            n = Grove(number, before, None)
            before.after = n
            before = n
            groves.append(before)
        n.after = first
        first.before = n

        return first

    def to_list(first):
        ret = [first]
        n = first.after
        while n != first:
            ret.append(n)
            n = n.after
        return ret

    def update(current: Grove, length):
        move = current.value
        if move % length == 0:
            return None
        elif move > 0:
            n = current.after
            for _ in range(move):
                n = n.after
        else:
            n = current.before
            for _ in range(- move - 1):
                n = n.before
        prev = n.before
        #print('cur', current.show())
        #print('prev', prev.show())
        #print('n', n.show())
        current.before.after = current.after
        current.after.before = current.before
        prev.after = current
        current.before = prev
        current.after = n
        n.before = current

    def update_all(input):
        for element in first:
            update(element, len(input))
        return to_list(input[0])

    first = to_list(add_groves(st))
    update_all(first)
    zero = None
    for el in first:
        if el.value == 0:
            zero = el
    print(zero.show())
    ans1 = 0
    for i in range(3000):
        zero = zero.after
        if (i + 1) % 1000 == 0:
            ans1 += zero.value
            print(zero.value)
    print(ans1)


if __name__ == '__main__':
    solve('day20.txt')
