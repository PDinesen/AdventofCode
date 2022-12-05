def solve(txt_name):
    st = [item.split(',') for item in [contents.rstrip('\n') for contents in open(txt_name)]]
    count = 0
    count2 = 0
    for item in st:
        elf1 = list(map(int, item[0].split('-')))
        elf2 = list(map(int, item[1].split('-')))
        if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]):
            count += 1
        if min(elf1[1], elf2[1]) - max(elf1[0], elf2[0]) >= 0:
            count2 += 1
    print('Day 4 part 1: ' + str(count))
    print('Day 4 part 2: ' + str(count2))


if __name__ == '__main__':
    solve('day4.txt')
