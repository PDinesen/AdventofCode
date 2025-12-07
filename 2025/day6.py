st = [item.split() for item in [content.rstrip('\n') for content in open('day6.txt')]]
st2 = [item for item in [content.rstrip('\n') for content in open('day6.txt')]]


numbers = st[:-1]
operations = st[-1]

resultatListe = []

for i in range(len(operations)):
    if operations[i] == '*':
        res = 1
        for number in numbers:
            res *= int(number[i])
    elif operations[i] == '+':
        res = 0
        for number in numbers:
            res += int(number[i])
    resultatListe.append(res)

print(sum(resultatListe))

temp = []
for i in range(max(len(st2[j]) for j in range(len(st2)))):
    line = ''
    for x in st2:
        if i >= len(x) or x[i] == ' ':
            continue
        line += x[i]
    temp.append(line)

resultatListe2 = []

for element in temp:
    if '*' in element or '+' in element:
        res = element[:-1]
        operation = element[-1]
    elif element == '':
        resultatListe2.append(eval(res))
    else:
        res += operation + element
resultatListe2.append(eval(res))

print(sum(resultatListe2))




