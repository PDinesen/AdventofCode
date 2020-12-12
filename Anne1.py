import AOCH

tal=AOCH.ril("input1-1")

tal=list(map(int,tal))

print(tal)

for i in tal:
    for j in tal:
        for k in tal:
            if k+i+j==2020:
                print(k*i*j)