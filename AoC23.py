from datetime import datetime

print(datetime.now() - datetime.now())

input_number = [8, 5, 3, 1, 9, 2, 6, 4, 7]
test = [3, 8, 9, 1, 2, 5, 4, 6, 7]


def move(list_input):
    current = list_input[0]
    picked = list_input[1:4]
    index = 0
    found = False
    while not found:
        if current == 1:
            current = max(list_input)
        else:
            current -= 1
        if current not in picked:
            index = list_input.index(current)
            found = True
    """
    print(list_input)
    print('current = ' + str(list_input[0]))
    print('picked = ', picked)
    print('Destination = ' + str(list_input[index]))
    """

    return list_input[4:index + 1] + picked + list_input[index + 1:] + list_input[:1]


def run(input_list, times):
    past = datetime.now()
    for i in range(times):
        if i % pow(10,2) == 0:
            print(i)
            print((datetime.now() - past).total_seconds())
            past = datetime.now()
        input_list = move(input_list)
    index = input_list.index(1)
    input_list = input_list[index + 1:] + input_list[: index]
    res = ''
    for item in input_list:
        res += str(item)
    return input_list[-1:] + input_list[:-1]


# print(run(test, 100))

# print(run(input_number, 100))


def run2(input_list, times):
    max_in_list = max(input_list)
    for i in range(max_in_list + 1, pow(10, 6) + 1):
        input_list.append(i)
    temp = run(input_list, times)
    print(temp[0], temp[1], temp[0] * temp[1])


run2(input_number, pow(10, 6))
run2(test, pow(10, 6))
max_test = max(test)
for i in range(10):
    test.append(max_test + 1 + i)

run(test, len(test) +1)
