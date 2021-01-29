filename = 'input2.txt'
data = [Line.split(',') for Line in open(filename)][0]

print(data)

def run(input_list, noun, verb):
    result = list(map(int, input_list.copy()))
    result[1] = noun
    result[2] = verb
    done = False
    i = 0
    while not done:
        if result[i] == 1:
            result[result[i+3]] = result[result[i+1]] + result[result[i+2]]
        elif result[i] == 2:
            result[result[i+3]] = result[result[i+1]] * result[result[i+2]]
        elif result[i] == 99:
            done = True
            break
        i += 4
    return result[0]

print(run(data, 12, 2))
def run2(data):
    for i in range(100):
        for j in range(100):
            if run(data, i, j) == 19690720:
                return 100 * i + j

print(run2(data))


