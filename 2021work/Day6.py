ind = [list(map(int,line.split(','))) for line in open('input6.txt')][0]
test=[3,4,3,1,2]

dict_fish = {}
for i in range(9):
    dict_fish[i] = sum(j == i for j in ind)

def one_day2(dictonary):
    zeros = dictonary[0]
    for key in range(1,9):
        fishes = dictonary[key]
        dictonary[key - 1] = fishes
    dictonary[6] += zeros
    dictonary[8] = zeros
    return dictonary

def run2(n, dict_fishes):
    temp = dict_fishes.copy()
    for _ in range(n):
        temp = one_day2(temp)
    print(sum(i for i in temp.values()))

run2(80,dict_fish)
run2(256,dict_fish)