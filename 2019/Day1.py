import AOCH

res = sum([int(int(item)/3)-2 for item in AOCH.ril('input1.txt')])
print(res)

sum_res = 0
for i in [int(item) for item in AOCH.ril('input1.txt')]:
    current = i
    while current > 5:
        current = int(current/3) -2
        sum_res += current
print(sum_res)



