st = [item for item in [contents.rstrip('\n') for contents in open('input/' + 'day2' + '.txt')]]
print(st)
color = ['red', 'green', 'blue']
st2 = []
for item in st:

    save = dict()
    for el in color:
        save[el] = []
    ID = item[4:item.index(':')]
    temp = list(el.split(',') for el in item[item.index(':')+1:].split(';'))
    for pick in temp:
        for col in pick:
            save[col.split(' ')[2]].append(int(col.split(' ')[1]))
            print(save)

    st2.append(save)
    print(item)

res = 0
res2 = 0
for i, pick in enumerate(st2):
    if max(pick['red']) <= 12 and max(pick['green']) <= 13 and max(pick['blue']) <= 14:
        res += i + 1
    res2 += max(pick['red']) * max(pick['green']) * max(pick['blue'])

print(res)
print(res2)