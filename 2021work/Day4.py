lines = [line.rstrip('\n') for line in open('input4.txt')]


def initial(input_lines):
    ins = list(map(int, input_lines[0].split(',')))
    boards = []
    board = []

    for line in input_lines[2:]:
        if line == '':
            boards.append(board)
            board = []
        else:
            temp2 = line.split(' ')
            temp3 = []
            for i in range(len(temp2)):
                if temp2[i] != '':
                    temp3.append(int(temp2[i]))
            board.append(temp3)
    return ins, boards


def c_board(used, table):
    not_used = []
    res, us = None, None
    for i in range(len(table)):
        r = True
        c = True
        temp_row = []
        temp_col = []
        for j in range(len(table)):
            temp_row.append(table[i][j])
            temp_col.append(table[j][i])
            if table[i][j] not in used:
                if table[i][j] not in not_used:
                    not_used.append(table[i][j])
                r = False
            if table[j][i] not in used:
                if table[j][i] not in not_used:
                    not_used.append(table[j][i])
                c = False
        if r:
            res, us = temp_row, used[-1]
        elif c:
            res, us = temp_col, used[-1]
    return res, us, not_used


def run(input_lines):
    ins, boards = initial(input_lines)
    used = []
    for inst in ins:
        used.append(inst)
        for board in boards:
            b, u, nu = c_board(used, board)
            if u is not None:
                print(u * sum(nu))


def run2(input_lines):
    instructions, input_boards = initial(input_lines)
    used = []
    b, u, nu = None, None, None
    for inst in instructions:
        used.append(inst)
        temp = []
        for table in input_boards:
            b, u, nu = c_board(used, table)
            if u is not None:
                temp.append(table)
        input_boards = temp
        if len(input_boards) == 0:
            print(u * sum(nu))
