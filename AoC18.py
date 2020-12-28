input18 = [line[:-1] for line in open('input18.txt')]


def find_levels(string_number):
    start = [i for i in range(len(string_number)) if string_number[i] == '(']
    end = [i for i in range(len(string_number)) if string_number[i] == ')']
    indexes = start + end
    levels = []
    level = 0
    while len(start) > 0:
        for i in range(len(start)):
            if i == len(start) - 1:
                return [start[i], end[0]]

            elif start[i+1] > end[0]:
                return [start[i], end[0]]


def update_string(level, string_number, func):
    new_string = func(string_number[level[0] + 1:level[1]])
    if level[0] == 0 and level[1] == len(string_number) - 1:
        string_number = new_string
    elif level[0] == 0:
        string_number = new_string + string_number[level[1] + 1:]
    elif level[1] == len(string_number) - 1:
        string_number = string_number[:level[0]] + new_string
    else:
        string_number = string_number[:level[0]] + new_string + string_number[level[1] + 1:]
    return string_number


def calculate(string_number):
    level = find_levels(string_number)
    if level is not None:
        return calculate(update_string(level, string_number, calculate))
    else:
        string_list = string_number.split(' ')
        res = 0
        plus = True
        for i in string_list:
            try:
                if plus:
                    res += int(i)
                else:
                    res *= int(i)
            except ValueError:
                if i == '+':
                    plus = True
                else:
                    plus = False
        return str(res)


print(calculate('(1 + 1 * 3) + ((2 + 3) + (4 * 5))'))
print(calculate(input18[1]))


def run(input_list):
    res = 0
    for number in input_list:
        res += int(calculate(number))

    return res


print(run(input18))


def calculate2(string_number):
    level = find_levels(string_number)
    if level is not None:
        return calculate2(update_string(level, string_number, calculate2))
    else:
        string_list = string_number.split(' ')
        res = 0
        plus = True
        temp = []
        for i in string_list:
            try:
                if plus:
                    res += int(i)
                else:
                    temp.append(res)
                    res = int(i)
                    plus = True
            except ValueError:
                if i == '+':
                    plus = True
                else:
                    plus = False
        temp.append(res)
        res = 1
        for i in temp:
            res *= i
        return str(res)


def run2(input_list):
    res = 0
    for number in input_list:
        # print(number + ' = ' + calculate2(number))
        res += int(calculate2(number))

    return res


print(run2(input18))

