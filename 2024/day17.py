st = [item for item in [content.rstrip('\n') for content in open('input/' + 'day17' + '.txt')]]

register = {}
instructions = None
for line in st:
    if line == '':
        continue
    elif line[0] == 'R':
        s = line.split(':')
        register[s[0]] = int(s[1])
    elif line[0] == 'P':
        instructions = line.split(': ')[1].split(',')


def get_combo(ins):
    if ins in '0123':
        return int(ins)
    elif ins == '4':
        return register['Register A']
    elif ins == '5':
        return register['Register B']
    elif ins == '6':
        return register['Register C']


def opcode(ins, ope, index):
    out = None
    if ins == '0':
        register['Register A'] = register['Register A'] // pow(2, get_combo(ope))
    elif ins == '1':
        register['Register B'] = xor(register['Register B'], int(ope))
    elif ins == '2':
        register['Register B'] = get_combo(ope) % 8
    elif ins == '3':
        if register['Register A'] != 0:
            return int(ope), out
    elif ins == '4':
        register['Register B'] = xor(register['Register B'], register['Register C'])
    elif ins == '5':
        # print(ope, get_combo(ope))
        out = str(get_combo(ope) % 8)
    elif ins == '6':
        register['Register B'] = register['Register A'] // pow(2, get_combo(ope))
    elif ins == '7':
        register['Register C'] = register['Register A'] // pow(2, get_combo(ope))
    return index + 2, out


def xor(a, b):
    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]
    diff = max(len(bin_a), len(bin_b))
    if len(bin_a) < len(bin_b):
        bin_a = '0'*(diff - len(bin_a)) + bin_a
    elif len(bin_b) < len(bin_a):
        bin_b = '0'*(diff - len(bin_b)) + bin_b

    bin_r = ''
    for i in range(diff):
        if bin_a[i] == bin_b[i]:
            bin_r += '0'
        else:
            bin_r += '1'
    return int(bin_r, 2)


def calc_a(t_list):
    a = 0
    for j in range(len(t_list)):
        a += t_list[j] * pow(8, j)
    return a


def find_a(instruction):
    t = [0]*len(instruction)
    t[-1] = 1
    r = run(calc_a(t))
    while instruction != r:
        for k in range(len(t) - 2, -1, -1):
            if r[k] != instruction[k]:
                te = False
                while not te:
                    if k > len(t) - 2:
                        return -1
                    t[k] = (t[k] + 1) % 8
                    te = t[k] != 0
                    k += 1
                break
        r = run(calc_a(t))
    return calc_a(t)


def run(a=register['Register A']):
    i = 0
    o_print = []
    register['Register A'] = a
    while i < len(instructions) - 1:
        i, out_print = opcode(instructions[i], instructions[i + 1], i)
        if out_print:
            o_print.append(out_print)

    return o_print


res = run()

print(",".join(res))
print(find_a(instructions))
