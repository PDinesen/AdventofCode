ind = [list(map(int, line.split(','))) for line in open('input7.txt')][0]

test = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

print(min(sum(abs(i-el) for el in ind) for i in range(max(ind))))
print(min(sum(int(((abs(i-el)+1)*abs(i-el))/2) for el in ind) for i in range(max(ind))))
