import AOCH

input5 = AOCH.ril("input5.txt")

print(input5)
maxi = 0
ID=[]
for i in input5:
    row = ''
    col = ''

    for j in i:
        if j=='F':
            row+='0'
        elif j=='B':
            row+='1'
        elif j=='R':
            col+='1'
        elif j=='L':
            col+='0'

    if int(row,2)*8+int(col,2)>maxi:
        maxi=int(row,2)*8+int(col,2)
    print(int(row,2),int(col,2),int(row,2)*8+int(col,2))
    ID.append(int(row,2)*8+int(col,2))


ID=sorted(ID)
for i in range(min(ID),max(ID)):
    if i not in ID:
        print(i)

print(maxi)
print(ID)

