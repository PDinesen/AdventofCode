input_lines = [line.rstrip('\n') for line in open('input8.txt')]

easy_digits_dict = {2: '1', 3: '7', 4: '4', 7: '8'}

number_of_easy_knowns = 0
sum_of_output = 0

for line in input_lines:
    input_data, output_data = line.split(' | ')

    input_values = input_data.split()
    output_values = output_data.split()

    # Digit analysis
    input_values.sort(reverse=False, key=len)
    one_lines = []
    nine_lines = []
    three_lines = []

    for i in input_values:

        if len(i) == 2:
            one_lines = list(i)

        if len(i) == 5 and min(k in i for k in one_lines) == 1:
            three_lines = list(i)

        if len(i) == 6 and min(k in i for k in three_lines) == 1:
            nine_lines = list(i)

    # Identification
    output_number = ''

    for o in output_values:

        if len(o) in easy_digits_dict.keys():
            number_of_easy_knowns += 1
            output_number += easy_digits_dict[len(o)]

        if len(o) == 5:
            if min(k in o for k in one_lines) == 1:
                output_number += '3'
            elif min(k in nine_lines for k in o) == 1:
                output_number += '5'
            else:
                output_number += '2'
        if len(o) == 6:
            if min(k in o for k in three_lines) == 1:
                output_number += '9'
            elif min(k in o for k in one_lines) == 1:
                output_number += '0'
            else:
                output_number += '6'

    sum_of_output += int(output_number)

assert number_of_easy_knowns == 272
print(f"Part 1: {number_of_easy_knowns}")

assert sum_of_output == 1007675
print(f"Part 2: {sum_of_output}")