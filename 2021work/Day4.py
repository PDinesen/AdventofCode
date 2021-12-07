lines = [line.rstrip('\n') for line in open('input4.txt')]
ins = list(map(int,lines[0].split(',')))
print(ins)

print(lines)
test = '2 0 2  3'

boards = []
board = []
for line in lines[2:]:
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

print(boards[0])


def c_board(used, board):
    not_used = []
    res, us = None, None
    for i in range(len(board)):
        r = True
        c = True
        temp_row = []
        temp_col = []
        for j in range(len(board)):
            temp_row.append(board[i][j])
            temp_col.append(board[j][i])
            if board[i][j] not in used:
                if board[i][j] not in not_used:
                    not_used.append(board[i][j])
                r = False
            if board[j][i] not in used:
                if board[j][i] not in not_used:
                    not_used.append(board[j][i])
                c = False
        if r:
            res, us = temp_row, used[-1]
        elif c:
            res, us = temp_col, used[-1]
    return (res, us, not_used)

t = c_board([27, 85, 56, 33, 1],[[85, 23, 65, 78, 93], [27, 53, 10, 12, 26], [5, 34, 83, 25, 6], [56, 40, 73, 29, 54], [33, 68, 41, 32, 82]])
print(t)

def run(ins, boards):
    used = []
    for inst in ins:
        used.append(inst)
        for board in boards:
            b,u,nu = c_board(used,board)
            if u != None:
                print('DONE')
                return (b,u,nu)

b,u,nu = run(ins,boards)
print(u*sum(nu))

print(boards.pop(0))
print(boards)

def run2(ins,boards):
    used = []
    for inst in ins:
        used.append(inst)
        temp = []
        for board in boards:
            b, u, nu = c_board(used, board)
            if u == None:
                temp.append(board)
        boards = temp
        if len(boards) == 0:
            return (b,u,nu)
    return None

b,u,nu = run2(ins,boards)
print(u*sum(nu))