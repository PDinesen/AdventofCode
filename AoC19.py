import AOCH


def initialize(filename):
    input19 = AOCH.ril2(filename, '')
    temp_set = {}
    for i in range(len(input19[0])):
        input19[0][i] = input19[0][i].split(': ')
        temp_list = input19[0][i][1].split(' | ')
        if len(temp_list) == 1:
            if len(temp_list[0].split(' ')) > 1:
                temp_set[input19[0][i][0]] = [temp_list[0].split(' ')]
            else:
                if temp_list[0][0] == '"':
                    temp_set[input19[0][i][0]] = temp_list[0].split('"')[1]
                else:
                    print('Here', temp_list)
                    temp_set[input19[0][i][0]] = [temp_list]
        else:
            for j in range(len(temp_list)):
                temp_list[j] = temp_list[j].split(' ')
            temp_set[input19[0][i][0]] = temp_list
    return [temp_set, input19[1]]



def pos(input_set, key_val='0'):
    try:
        temp = []
        for item1 in input_set[key_val]:
            temp1 = []
            for val in item1:
                temp3 = []
                if len(temp1) == 0:
                    for item2 in pos(input_set, val):
                        temp1.append(item2)
                else:
                    for i in range(len(temp1)):
                        for item2 in pos(input_set, val):
                            temp3.append(temp1[i] + item2)
                    temp1 = temp3.copy()
            for item3 in temp1:
                temp.append(item3)

        return temp

    except KeyError:
        return [input_set[key_val]]


def run(filename, start_val= '0'):
    input_list = initialize(filename)
    tjek_list = pos(input_list[0], start_val)
    print(tjek_list)
    count = 0
    for item in input_list[1]:
        if item in tjek_list:
            count += 1
    print(count)
    return count

# input19 = initialize('input19.txt')
# print(input19[0]['0'])
# print(pos(input19[0], '42'))
# run('input19.txt')

print('asdf'.index('a'))
val = '112345'
print(val[len(val):] == '')


def run2(filename):
    input_list = initialize(filename)
    test1 = pos(input_list[0], '42')
    length1 = len(test1[0])
    test2 = pos(input_list[0], '31')
    length2 = len(test2[0])
    count = 0
    for value in input_list[1]:
        count1 = 0
        count2 = 0
        if len(value) >= length1:
            first = True
            while first:
                if value[:length1] in test1:
                    value = value[length1:]
                    count1 += 1
                else:
                    first = False
                if len(value) < length1:
                    first = False
        if len(value) >= length2:
            second = True
            while second:
                if value[:length2] in test2:
                    value = value[length2:]
                    count2 += 1
                    count1 -= 1
                else:
                    second = False
                if len(value) < length2:
                    second = False
        if value == '' and count1 > 0 and count2 > 0:
            count += 1
    print(count)
    return count


run2('input19.txt')



"""

print(1, pos(input19[0], '1'))
print(2, pos(input19[0], '2'))
print(3, pos(input19[0], '3'))
print(4, pos(input19[0], '4'))
print(5, pos(input19[0], '5'))

print(input19[0])
print(input19[0]['0'])
print(input19[0]['4'][0], input19[0]['1'], input19[0]['5'])
print(input19[0]['4'], [[input19[0]['2'], input19[0]['3']], [input19[0]['3'], input19[0]['2']]], input19[0]['5'])
temp = ['a', [[[['aa', 'bb'], ['ab', 'ba']], [['ab', 'ba'], ['aa', 'bb']]]], 'b']
for i in temp:
    print(i)

for item in range(len(input19[0])):
    for val in input19[0][item]:
        if input19[0][val] not in ['a', 'b']:
            for item1 in input19[0][val]:
                for val1 in item1:
                    print(input19[0][val1])
        print(input19[0][val])
"""