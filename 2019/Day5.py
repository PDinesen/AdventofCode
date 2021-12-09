filename = 'input5.txt'
data = [Line.split(',') for Line in open(filename)][0]

print(data)
test = ['1', '2', '102', '99', '1002', '103', '104']


def get_instructions(instruct):
    length = len(instruct)
    parameters = ['0'] * 4
    if length == 1:
        parameters[0] = '0' + instruct
    elif length == 2:
        parameters[0] = instruct
    else:
        parameters[0] = instruct[-2:]
        for i in range(2, len(instruct)):
            parameters[i-1] = instruct[-i-1]
    return parameters


def run(input_list, ID):
    result = input_list.copy()
    i = 0
    while True:
        instructions = get_instructions(result[i])
        if instructions[0] == '99':
            return result

        if instructions[1] == '0':
            first_input = int(result[int(result[i + 1])])
        else:
            first_input = int(result[i + 1])
        if instructions[0] in ('01', '02', '05', '06', '07', '08'):
            if instructions[2] == '0':
                second_input = int(result[int(result[i + 2])])
            else:
                second_input = int(result[i + 2])

        if instructions[0] == '01':
            result[int(result[i + 3])] = str(first_input + second_input)
            prev = result[i:i+4]
            i += 4
        elif instructions[0] == '02':
            result[int(result[i + 3])] = str(first_input * second_input)
            prev = result[i:i+4]
            i += 4
        elif instructions[0] == '03':
            result[int(result[i + 1])] = str(ID)
            prev = result[i:i+2]
            i += 2
        elif instructions[0] == '04':
            print(first_input)
            prev = result[i:i+2]
            i += 2
        elif instructions[0] == '05':
            if first_input != 0:
                i = second_input
            else:
                i += 3
        elif instructions[0] == '06':
            if first_input == 0:
                i = second_input
            else:
                i += 3
        elif instructions[0] == '07':
            if first_input < second_input:
                result[int(result[i + 3])] = '1'
            else:
                result[int(result[i + 3])] = '0'
            i += 4
        elif instructions[0] == '08':
            if first_input == second_input:
                result[int(result[i + 3])] = '1'
            else:
                result[int(result[i + 3])] = '0'
            i += 4
        elif instructions[0] == '99':
            break


print(run(data, 1))
print(data)

test1 = list(map(str, [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]))
print(test1)
run(test1,9)

run(data, 5)