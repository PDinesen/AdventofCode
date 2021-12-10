import statistics
ind = [line.rstrip('\n') for line in open('input10.txt')]

points1 = {')': 3,
           ']': 57,
           '}': 1197,
           '>': 25137}

points2 = {'(': 1,
           '[': 2,
           '{': 3,
           '<': 4}


def remove_goodies(string):
    temp = ''
    while temp != string:
        temp = string
        for par in ['()', '[]', '{}', '<>']:
            string = string.replace(par, '')
    return string


def run(input_string):
    ans1 = 0
    ans2_list = []
    temp2 = input_string.copy()
    for item in input_string:
        temp = remove_goodies(item)
        for char in temp:
            if char in [')', ']', '}', '>']:
                ans1 += points1[char]
                temp2.remove(item)
                break
    print(ans1)

    for item in temp2:
        total = 0
        temp = remove_goodies(item)
        for char in temp[::-1]:
            total *= 5
            total += points2[char]
        ans2_list.append(total)
    ans2_list.sort()
    print(statistics.median(ans2_list))


if __name__ == '__main__':
    run(ind)
