import AOCH

input6 = AOCH.ril('input6.txt')
test = ['abc','cde','','aaf','a']
print(input6)
test = AOCH.ril2('input6.txt', '')
print(test)
def run(input6):
    count = 0
    temp = []


    for i in input6:
        if i == '':
            count += len(temp)
            temp = []
        else:
            for j in i:
                if j not in temp:
                    temp.append(j)
    count += len(temp)
    return count


print(run(input6))
print('j' in 'ja')
print(AOCH.group(input6,'')[0])

def run2(input):
    count = 0
    for i in input:
        temp=[]
        for j in range(len(i)):
            for k in i[j]:
                inall = True
                for l in range(len(i)):
                    if k not in i[l] or k in temp:
                        inall = False
                        continue
                if inall:
                    temp.append(k)
        count += len(temp)
    return count

print(run2(AOCH.group(test,'')))
print(AOCH.group(input6,''))
print(run2(AOCH.group(input6,'')))