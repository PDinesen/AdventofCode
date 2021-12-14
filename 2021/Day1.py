def input_file(txt_name):
    return [int(item) for item in [contents.rstrip('\n') for contents in open(txt_name)]]


def answer(txt_name, n, task_number):
    numbers = input_file(txt_name)
    print(numbers)
    ans = sum(numbers[i] < numbers[i+n] for i in range(len(numbers)-n))
    print('task ' + str(task_number) + ' : ' + str(ans))
    return 0


if __name__ == '__main__':
    answer('input1.txt', 1, 1)
    answer('input1.txt', 3, 2)
