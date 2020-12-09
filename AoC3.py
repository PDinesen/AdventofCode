import AOCH

input3 = AOCH.ril("input3.txt")

print(input3[0][0])


pos = [0,0]
count1 = 0
l = len(input3[pos[0]])
run = True
while run:
    pos[1] = pos[1] % l
    if input3[pos[0]][pos[1]] == '#':
        count1 += 1
    pos[0] += 1
    pos[1] += 1
    if pos[0] == len(input3):
        run = False


pos = [0,0]
count2 = 0
l = len(input3[pos[0]])
run = True
while run:
    pos[1] = pos[1] % l
    if input3[pos[0]][pos[1]] == '#':
        count2 += 1
    pos[0] += 1
    pos[1] += 3
    if pos[0] == len(input3):
        run = False

pos = [0,0]
count3 = 0
l = len(input3[pos[0]])
run = True
while run:
    pos[1] = pos[1] % l
    if input3[pos[0]][pos[1]] == '#':
        count3 += 1
    pos[0] += 1
    pos[1] += 5
    if pos[0] == len(input3):
        run = False

pos = [0,0]
count4 = 0
l = len(input3[pos[0]])
run = True
while run:
    pos[1] = pos[1] % l
    if input3[pos[0]][pos[1]] == '#':
        count4 += 1
    pos[0] += 1
    pos[1] += 7
    if pos[0] == len(input3):
        run = False

pos = [0,0]
count5 = 0
l = len(input3[pos[0]])
run = True
while run:
    pos[1] = pos[1] % l
    if input3[pos[0]][pos[1]] == '#':
        count5 += 1
    pos[0] += 2
    pos[1] += 1
    if pos[0] >= len(input3):
        run = False

print(count1,count2,count3,count4,count5,count4*count5*count3*count1*count2)