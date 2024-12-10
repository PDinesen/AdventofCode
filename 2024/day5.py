st = [item for item in [contents.rstrip('\n') for contents in open('input/' + 'day5' + '.txt')]]

rules_dict = dict()
rules = []
updates = []
rule = True
for line in st:
    if line == '':
        rule = False
    elif rule:
        temp = line.split('|')
        if temp[0] in rules_dict.keys():
            rules_dict[temp[0]].append(temp[1])
        else:
            rules_dict[temp[0]] = [temp[1]]
        rules.append(line.split('|'))
    else:
        updates.append(line.split(','))


def bad(update):
    for i in range(len(update)-1, 0, -1):
        for j in update[:i]:
            if update[i] in rules_dict.keys() and j in rules_dict[update[i]]:
                return True
    return False


def move_last_error(update):
    for i in range(len(update)-1, 0, -1):
        for j in range(len(update[:i])):
            if update[i] in rules_dict.keys() and update[j] in rules_dict[update[i]]:
                update.insert(j, update.pop(i))
                return update
    return update


def fix_it(update):
    fix = update
    while bad(fix):
        fix = move_last_error(fix)
    return fix


result = 0
result2 = 0

for up in updates:
    if not bad(up):
        result += int(up[len(up)//2])
    else:
        fixed = fix_it(up)
        result2 += int(fixed[len(fixed)//2])


print(result)
print(result2)
