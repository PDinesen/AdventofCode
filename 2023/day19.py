from copy import deepcopy
from math import prod
st = [c.rstrip('\n') for c in open('input/' + 'day19' + '.txt')]


def parse_data(lst):
    rules = dict()
    metal = []
    split = False
    for line in lst:
        if line == '':
            split = True
            continue
        if split:
            metal.append({x[0]: int(x[1]) for x in [lines.split('=') for lines in line[1:-1].split(',')]})
        else:
            rules[line[:line.index('{')]] = [x.split(':') for x in line[line.index('{'):][1:-1].split(',')]

    return metal, rules


def parse_rule(metal, rule):
    for el in rule:
        if len(el) == 1:
            return el[0]
        if '<' in el[0]:
            x = el[0].split('<')
            if metal[x[0]] < int(x[1]):
                return el[1]
        elif '>' in el[0]:
            x = el[0].split('>')
            if metal[x[0]] > int(x[1]):
                return el[1]


def solution(lst):
    metal, rules = parse_data(lst)
    res = 0
    for m in metal:
        rule = 'in'
        while rule not in 'AR':
            rule = parse_rule(m, rules[rule])
        if rule == 'A':
            res += sum(m.values())
    print(res)


solution(st)


def parse_range(metal_range, rules, rule='in'):
    lst_range = 0
    if rule == 'A':
        return prod(x[1]-x[0] + 1 for x in metal_range.values())
    elif rule == 'R':
        return 0
    for el in rules[rule]:
        if len(el) == 1:
            lst_range += parse_range(metal_range, rules, el[0])
        if '<' in el[0]:
            x = el[0].split('<')
            if max(metal_range[x[0]]) < int(x[1]):
                lst_range += parse_range(metal_range, rules, el[1])
            elif min(metal_range[x[0]]) < int(x[1]):
                nrl = deepcopy(metal_range)
                nrl[x[0]], metal_range[x[0]] = [min(metal_range[x[0]]), int(x[1]) - 1], \
                                               [int(x[1]), max(metal_range[x[0]])]
                lst_range += parse_range(nrl, rules, el[1])
        elif '>' in el[0]:
            x = el[0].split('>')
            if min(metal_range[x[0]]) > int(x[1]):
                lst_range += parse_range(metal_range, rules, el[1])
            elif max(metal_range[x[0]]) > int(x[1]):
                nrh = deepcopy(metal_range)
                metal_range[x[0]], nrh[x[0]] = [min(metal_range[x[0]]), int(x[1])], \
                                               [int(x[1]) + 1, max(metal_range[x[0]])]
                lst_range += parse_range(nrh, rules, el[1])
    return lst_range


def solution2(lst):
    _, rules = parse_data(lst)
    rg = [1, 4000]
    metal_range = {'x': rg, 'm': rg, 'a': rg, 's': rg}
    lst_range = parse_range(metal_range, rules)
    print(lst_range)


solution2(st)
