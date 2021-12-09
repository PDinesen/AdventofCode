def input_file(txt_name):
    return [line.split(' ') for line in [item.rstrip('\n') for item in open(txt_name)]]


def answer(txt_name):
    ins = input_file(txt_name)
    h = 0
    d = 0
    a = 0
    for item in ins:
        if item[0] == 'forward':
            h += int(item[1])
            d += a * int(item[1])
        elif item[0] == 'down':
            a += int(item[1])
        else:
            a -= int(item[1])
    print('task 1 : ' + str(h*a))
    print('task 2 : ' + str(h*d))


if __name__ == '__main__':
    answer('input2.txt')
