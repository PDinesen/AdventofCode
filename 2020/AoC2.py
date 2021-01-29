import AOCH
from AOCHelper import day2

input2 = AOCH.password_input("input2")
input2 = day2('input2')

count_t = 0
count_t2 = 0
for item in input2:
    count_l = 0
    letter = item[1][0]
    if (letter == item[2][item[0][0] - 1] and letter != item[2][item[0][1] - 1]) or \
            (letter != item[2][item[0][0] - 1] and letter == item[2][item[0][1] - 1]):
        count_t2 += 1
    for j in item[2]:
        if letter == j:
            count_l += 1
    if item[0][1] >= count_l >= item[0][0]:
        count_t += 1

print(count_t, count_t2)
