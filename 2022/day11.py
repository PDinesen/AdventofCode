def solve(txt_name, part1=True):
    st = [item for item in [contents.rstrip('\n') for contents in open(txt_name)]]
    if part1:
        n = 20
    else:
        n = 10000

    class Monkey:
        def __init__(self, name: str, item: list, operation: str, test_crit: int, test_to: list):
            self.name = name
            self.items = item
            self.operation = operation
            self.test = test_crit
            self.test_to = test_to
            self.inspected = 0

        def operate(self, mode2):
            self.inspected += len(self.items)
            for num in range(len(self.items)):
                operation = self.operation.replace('old', str(self.items[num]))
                if part1:
                    self.items[num] = eval(operation) // 3
                else:
                    self.items[num] = eval(operation) % mode2

        def testing(self, it):
            if it % self.test == 0:
                return self.test_to[0]
            else:
                return self.test_to[1]

        def all_thrown(self):
            self.items = []

        def add_item(self, it):
            self.items.append(it)

        def show(self):
            print(self.name)
            print(self.items)
            print(self.operation)
            print(self.test)
            print(self.test_to)

    monkeys = dict()
    mode_2 = 1
    for i in range(0, (len(st) + 1) // 7):
        items = [int(item) for item in st[1 + i * 7][len('  Starting items: '):].split(',')]
        oper = st[2 + i * 7][len('  Operation: new = '):]
        test = int(st[3 + i * 7][len('  Test: divisible by '):])
        mode_2 *= test
        test_to_list = [st[4 + i * 7][len('    If true: throw to monkey '):],
                        st[5 + i * 7][len('    If false: throw to monkey '):]]

        monkey = Monkey(str(i), items, oper, test, test_to_list)
        monkeys[str(i)] = monkey
    for _ in range(n):
        for monkey in monkeys.values():
            monkey.operate(mode_2)
            for item in monkey.items:
                monkeys[monkey.testing(item)].add_item(item)
            monkey.all_thrown()

    ans = sorted(list(monkey.inspected for monkey in monkeys.values()))
    print(ans[-2] * ans[-1])


if __name__ == '__main__':
    solve('day11.txt')
    solve('day11.txt', False)
