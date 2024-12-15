

def is_safe(listen):
    good = True
    if listen[0] < listen[-1]:
        for i in range(0, len(listen) - 1):
            if listen[i + 1] - listen[i] not in [1, 2, 3]:
                good = False
    else:
        for i in range(0, len(listen) - 1):
            if listen[i] - listen[i + 1] not in [1, 2, 3]:
                good = False
    return good


if __name__ == '__main__':
    st = [list(map(int, item.split(' '))) for item in
          [contents.rstrip('\n') for contents in open('input/' + 'day2' + '.txt')]]

    safe = 0
    safe2 = 0
    for item in st:
        if is_safe(item):
            safe += 1
        else:
            for j in range(len(item)):
                if is_safe(item[:j] + item[j + 1:]):
                    safe2 += 1
                    break

    print('Part 1 \n' + str(safe))
    print('Part 2 \n' + str(safe + safe2))
