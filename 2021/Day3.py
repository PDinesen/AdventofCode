def Split(word):
    return [char for char in word]


def input_file(txt_name):
    return [list(map(int, Split(char))) for char in [item.rstrip('\n') for item in open(txt_name)]]


ind = input_file('input3.txt')

h = len(ind[0])
v = len(ind)




new_numbers = [0] * h
for item in ind:
    for i in range(h):
        new_numbers[i] += item[i]

eps = ''
gam = ''

for num in new_numbers:
    if num > v/2.:
        eps += '1'
        gam += '0'
    else:
        eps += '0'
        gam += '1'

print(int(eps,2)*int(gam,2))

def add_lists(lists_to_add):
    temp = [0]*len(lists_to_add[0])
    for item in lists_to_add:
        for i in range(len(lists_to_add[0])):
            temp[i] += item[i]
    return temp


def answer(my_lists, crit):
    res = my_lists
    keep = 0
    for i in range(len(res[0])):
        added = add_lists(res)
        if crit == 'eps':
            if added[i] >= len(res)/2.:
                keep = 1
            else:
                keep = 0
        elif crit == 'ox':
            if added[i] < len(res)/2.:
                keep = 1
            else:
                keep = 0
        temp = res.copy()
        for item in temp:
            if item[i] != keep:
                res.remove(item)
        if len(res) == 1:
            return res[0]


eps = answer(ind.copy(), 'eps')
oxy = answer(ind.copy(), 'ox')

print(int(''.join(map(str,eps)),2) * int(''.join(map(str,oxy)),2))

test = [[1,0,1,1],[1,1,0,0]]


