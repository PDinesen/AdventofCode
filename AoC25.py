import AOCH


def run(filename, init_sub):
    pub = list(map(int, AOCH.ril(filename)))
    init = 1
    i = 0
    while init != pub[0]:
        init *= init_sub
        init = init % 20201227
        i += 1
    init = 1
    for _ in range(i):
        init *= pub[1]
        init = init % 20201227
    print(init)
    return init


run('input25.txt', 7)

