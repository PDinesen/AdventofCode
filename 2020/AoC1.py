import AOCH
from AOCHelper import day1

input_list = AOCH.ril("input01")
input_list = AOCH.stt(input_list)

for i in range(0, len(input_list)):
    for j in range(i+1, len(input_list)):
        for k in range(j+1, len(input_list)):
            if input_list[i] + input_list[j] + input_list[k] == 2020:
                print([input_list[i], input_list[j], input_list[k], input_list[i] + input_list[j] + input_list[k],
                       input_list[i] * input_list[j] * input_list[k]])
