import AOCH

input2 = AOCH.password_input("input2-1")

print(input2)

count_t = 0
count_t2 = 0
for i in input2:
    count_l = 0
    letter = i[1][0]
    print(i)
    if (letter == i[2][i[0][0]-1] and letter != i[2][i[0][1]-1]) or \
            (letter != i[2][i[0][0]-1] and letter == i[2][i[0][1]-1]):
        count_t2 += 1
    for j in i[2]:
        if letter == j:
            count_l += 1
    if i[0][1] >= count_l >= i[0][0]:
        count_t += 1

print(count_t, count_t2)
