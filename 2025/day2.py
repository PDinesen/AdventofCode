st = [item.split('-') for item in [contents.split(',') for contents in open('day2.txt')][0]]
print(st)

def findpathern1(num: str):
     if len(num) % 2 == 1:
          return False
    #  print(num[:len(num)//2], num[len(num)// 2:])
     if num[:len(num)//2] == num[len(num)// 2:]:
          return True

def findpathern(num: str):
    for j in range(1, len(num)//2 + 1):
            if len(num) % (j) == 0:
                pathern = num[:j]
                k = j
                invalid = False
                while k < len(num) and not invalid:
                    # print(k, j, len(number))
                    # print(pathern, number[k:k + j])
                    if pathern != num[k:k + j]:
                        # print('er')
                        invalid = True
                    k += j
                # print(invalid, number)
                if not invalid:
                    # print('found ' + num)
                    return True
    return False

ans = 0
for r in st:
    
    for i in range(int(r[0]), int(r[1]) + 1):
        number = str(i)
        if findpathern(number):
             ans += i

print(ans)


