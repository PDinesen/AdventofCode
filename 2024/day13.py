st = [item for item in [content.rstrip('\n') for content in open('input/' + 'day13' + '.txt')]]

machines = []
machine = []
for line in st:
    if line == '':
        machines.append(machine)
        machine = []
    elif line[0] == 'B':
        machine.append((int(line[line.index('X+') + 2: line.index(',')]), int(line[line.index('Y+') + 2:])))
    elif line[0] == 'P':
        machine.append((int(line[line.index('X=') + 2: line.index(',')]), int(line[line.index('Y=') + 2:])))

machines.append(machine)


def solve(AB, BB, price):
    a1, a2 = AB
    b1, b2 = BB
    m, n = price
    B = (a2 * m - a1 * n)/(a2 * b1 - a1 * b2)
    A = (m - b1 * B)/a1
    return A, B


def run(machs, adder):
    res = 0
    for m in machs:
        A, B = solve(m[0], m[1], (adder + m[2][0], adder + m[2][1]))
        if A % 1 == 0 and B % 1 == 0:
            res += 3 * int(A) + int(B)
    return res


print(run(machines, 0))
print(run(machines, 10_000_000_000_000))
