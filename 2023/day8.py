from functools import reduce
from math import gcd
from regex import findall


def lcm(deno):
    return reduce(lambda a, b: a * b // gcd(a, b), deno)


st = [item for item in [contents.rstrip('\n') for contents in open('input/' + 'day8' + '.txt')]]

instr = st[0]
move = {item.split(' = ')[0]: findall(r'\w+', item.split(' = ')[1]) for item in st[2:]}


def find_steps(_start, _end):
    _found = False
    _steps = 0

    while not _found:
        for direction in instr:
            _steps += 1
            if direction == 'L':
                _start = move[_start][0]
            else:
                _start = move[_start][1]
            if _start.endswith(_end):
                _found = True
                break

    return _steps


ans1 = find_steps('AAA', 'ZZZ')

print(ans1 == 20093)

# Part 2

start_nodes = [node for node in move if node.endswith('A')]

ans2 = lcm(find_steps(node, 'Z') for node in start_nodes)

print(ans2 == 22103062509257)
