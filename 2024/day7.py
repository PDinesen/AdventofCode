import itertools as it

st = [item for item in [contents.rstrip('\n') for contents in open('input/' + 'day7' + '.txt')]]

s = 0
def komb(n):
    print(list(it.product(['+', '*'], repeat=n-1)))

komb(4)

for line in st:
    res, rest = int(line.split(': ')[0]), list(map(int, line.split(': ')[1].split(' ')))
    for ops in list(it.product(['+', '*', '|'], repeat=len(rest)-1)):
        resultat = rest[0]
        for i in range(len(ops)):
            if ops[i] == '+':
                resultat += rest[i+1]
            elif ops[i] == '*':
                resultat *= rest[i+1]
            else:
                resultat = int(str(resultat) + str(rest[i+1]))
        if resultat == res:
            s += resultat
            break

print(s)
