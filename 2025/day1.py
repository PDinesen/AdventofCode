st = [item for item in [contents.rstrip('\n') for contents in open('day1.txt')]]
start = 50
code1 = 0
code2 = 0
dirmap = {'L': -1, 'R': 1}
for i in st:
    dir = dirmap[i[0]]
    times = int(i[1::])
    code2 += abs((start + dir * times) // 100)
    if start == 0 and dir == -1:
        code2 -= 1
    start = (start + dir * times) % 100
    if start == 0:
        code1 += 1
        if dir == -1:
            code2 += 1
        

print(code1 == 1182, code2 == 6907)