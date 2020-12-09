import AOCH

input9 = AOCH.ril('input9.txt')


print(input9)

for i in range(len(input9)):
    input9[i] = int(input9[i])

def vallist(itemlist):
    temp = []
    for i in range(len(itemlist)):
        for j in range(len(itemlist)):
            temp.append(itemlist[i] + itemlist[j])
    return temp


def run(itemlist, valint):
    for i in range(valint, len(itemlist)):
        if itemlist[i] not in vallist(itemlist[i-valint:i]):
            return itemlist[i]
    return 0


def test(vallist, test):
    temp = []
    for i in vallist:
        temp.append(i - test)
    return temp


def sumf(itemlist):
    sum = 0
    for i in itemlist:
        sum += i

    return sum


def smallestlarges(itemlist):
    sm = itemlist[0]
    lar = itemlist[0]
    for i in itemlist:
        if i < sm:
            sm = i
        elif i > lar:
            lar = i
    return sm + lar

print(smallestlarges([10,20,30]))


def run2(itemlist, valint):
    number = run(itemlist, valint)
    for i in range(len(itemlist)):
        for j in range(i):
            if sumf(itemlist[i-j:i]) == number:
                return smallestlarges(itemlist[i-j:i])


    return 0


print(run2(input9, 25))

