from collections import Counter
from time import time

ind = [line.rstrip('\n') for line in open('input14.txt')]


ind_string = ind.pop(0)
ind.pop(0)
temp = {}
for item in ind:
    x, y = tuple(item.split(' -> '))
    temp[x] = y


def step(ind_string, rules):
    new_string = ''
    for i in range(len(ind_string) - 1):
        if ind_string[i:i+2] in rules.keys():
            new_string += ind_string[i] + rules[ind_string[i:i+2]]
        else:
            new_string += ind_string[i]
    new_string += ind_string[-1]
    return new_string


def make_n_step_rules(rules, n):
    temp = {}
    for rule in rules.keys():
        ans_string = rule
        for _ in range(n):
            ans_string = step(ans_string, rules)
        temp[rule] = ans_string[1:-1]
    return temp


def run(ind_string, rules, n):
    temp1 = ind_string
    for _ in range(n):
        temp1 = step(temp1, rules)
    letters = Counter(temp1)
    print(max(letters.values()) - min(letters.values()))


def run2(ind_string, rules, n1):
    rules = make_n_step_rules(rules, n1)
    temp3 = {item1: [Counter(rules[item1])] for item1 in rules.keys()}
    temp1 = step(ind_string, rules)
    c = Counter(temp1)
    for i in range(len(temp1) - 1):
        c += temp3[temp1[i:i+2]][0]
    ans = max(c.values()) - min(c.values())
    print(ans)


def recursive(first, last, rules, count, n, i=0):
    if i == n:
        return 0
    middel = rules[first + last]
    count.update(middel)
    recursive(first, middel, rules, count, n, i + 1)
    recursive(middel, last, rules, count, n, i + 1)
    return count


def run_new(ind_string, rules, n):
    temp1 = Counter(ind_string)
    for i in range(len(ind_string) - 1):
        first = ind_string[i]
        last = ind_string[i+1]
        temp1 = recursive(first, last, rules, temp1, n)
    print(temp1)
    print(max(temp1.values()) - min(temp1.values()))

t = time()
run_new(ind_string, temp, 10)
print(time() - t)
t = time()
run2(ind_string, temp, 20)
print(time() - t)



