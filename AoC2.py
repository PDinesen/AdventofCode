import AOCH

input2 = AOCH.passwordinput("input2-1")

print(input2)

countt = 0
countt2 = 0
for i in input2:
    countl = 0
    letter = i[1][0]
    print(i)
    if (letter == i[2][i[0][0]-1] and letter != i[2][i[0][1]-1]) or (letter != i[2][i[0][0]-1] and letter == i[2][i[0][1]-1]):
        countt2 += 1
    for j in i[2]:
        if letter == j:
            countl += 1
    if countl <= i[0][1] and countl >= i[0][0]:
        countt += 1

print(countt,countt2)