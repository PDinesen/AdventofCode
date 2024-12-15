import itertools as it

st = [item for item in [contents.rstrip('\n') for contents in open('input/' + 'day7' + '.txt')]]

s = 0


def comb(n):
    print(list(it.product(['+', '*'], repeat=n - 1)))


for line in st:
    res, rest = int(line.split(': ')[0]), list(map(int, line.split(': ')[1].split(' ')))
    for ops in list(it.product(['+', '*', '|'], repeat=len(rest) - 1)):
        result = rest[0]
        for i in range(len(ops)):
            if ops[i] == '+':
                result += rest[i + 1]
            elif ops[i] == '*':
                result *= rest[i + 1]
            else:
                result = int(str(result) + str(rest[i + 1]))
        if result == res:
            s += result
            break

print(s)
