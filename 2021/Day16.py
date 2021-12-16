ind = [i for i in open('input16.txt')][0]


def hex_to_bin(h):
    return bin(int(h, 16))[2:].zfill(len(h) * 4)


def get_att(h, count_v, binary=False):
    if binary:
        s = h
    else:
        s = hex_to_bin(h)
    v, s = int(s[0:3], 2), s[3:]
    t, s = int(s[0:3], 2), s[3:]
    pack = None
    count_v += v
    if t == 4:
        id_i = True
        pack = ''
        while id_i:
            id_i = s[0] == '1'
            pack += s[1:5]
            s = s[5:]
        return int(pack, 2), s, count_v
    else:
        if s[0] == '0':
            l, s = int(s[1:16], 2), s[16:]
            count, new = len(s), len(s)
            packs = []
            while count - new < l:
                pack, s, count_v = get_att(s, count_v, True)
                packs.append(pack)
                new = len(s)
            pack = packs
        elif s[0] == '1':
            l, s = int(s[1:12], 2), s[12:]
            packs = []
            for _ in range(l):
                pack, s, count_v = get_att(s, count_v, True)
                packs.append(pack)
            pack = packs
        if t == 0:
            pack = sum(pack)
        elif t == 1:
            temp = 1
            for item in pack:
                temp *= item
            pack = temp
        elif t == 2:
            pack = min(pack)
        elif t == 3:
            pack = max(pack)
        elif t == 5:
            if pack[0] > pack[1]:
                pack = 1
            else:
                pack = 0
        elif t == 6:
            if pack[0] < pack[1]:
                pack = 1
            else:
                pack = 0
        elif t == 7:
            if pack[0] == pack[1]:
                pack = 1
            else:
                pack = 0

    return pack, s, count_v


def run(h):
    pack, _, count = get_att(h, 0)
    print('Part 1: ' + str(count))
    print('Part 2: ' + str(pack))


if __name__ == '__main__':

    ''''
    run('38006F45291200')
    
    run('EE00D40C823060')
    
    run('8A004A801A8002F478')
    
    run('620080001611562C8802118E34')
    
    run('C0015000016115A2E0802F182340')
    
    run('A0016C880162017C3686B18A3D4780')
    '''

    run(ind)
