ind = [item.split(' | ')[1].split(' ') for item in [line.rstrip('\n') for line in open('input8.txt')]]
count = 0
for item in ind:
    count += sum(len(i) in [2, 3, 4, 7] for i in item)

print(count)

ind2 = [item.split(' | ') for item in [line.rstrip('\n') for line in open('input8.txt')]]
zero = 'abcefg'
one = 'cf'
two = 'acdeg'
tree = 'acdfg'
four = 'bcdf'
five = 'abdfg'
six = 'abdefg'
seven = 'acf'
eight = 'abcdefg'
nine = 'abcdfg'

temp = [zero, one, two, tree, four, five, six, seven, eight, nine]


def remove_number(n1, n2):
    return [i for i in n1 if i not in n2]


def find_number(list_numbers):
    temp = list_numbers
    check_list = [7, 32, 15, 10, 19, 12, 8, 24, 0, 4]
    ans = {}
    for item in temp:
        number = sum(len(remove_number(item2, item)) for item2 in temp)
        ans[''.join(sorted(item))] = check_list.index(number)
    return ans




def run(input_list):
    ans = 0
    for line in input_list:
        temp1 = line[0].split(' ')
        temp2 = line[1].split(' ')
        numbers = find_number(temp1)
        answer = ''
        for item in temp2:
            answer += '{}'.format(numbers[''.join(sorted(item))])
        ans += int(answer)

    print(ans)


run(ind2)

