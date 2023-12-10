st = [list(map(int, line.split())) for line in [contents.rstrip('\n') for contents in open('input/' + 'day9' + '.txt')]]

ans1 = 0
ans2 = 0
for line in st:
    ans1 += line[-1]
    ans2 += line[0]
    times = -1
    while not all(line[i] == line[i + 1] for i in range(len(line) - 1)):
        line = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        ans1 += line[-1]
        ans2 += line[0] * times
        times *= -1


print(ans1)
print(ans2)
