st = [item for item in [contents.rstrip('\n') for contents in open('day3.txt')]]

def volt(b: str, n: int):
    high = ''
    indexNow = -1
    for i in range(n):
        numberToAdd = str(max([int(i) for i in b[indexNow + 1:len(b) - (n - 1 - i)]]))
        indexNow += b[indexNow + 1:].index(numberToAdd) + 1
        high += numberToAdd
    #print(high)
    return high


ans = 0
for bank in st:
    ans += int(volt(bank, 2))

ans2 = 0
for bank in st:
    ans2 += int(volt(bank, 12))

print(ans)
print(ans2)