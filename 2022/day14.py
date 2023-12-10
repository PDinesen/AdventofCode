def solve(txt_name):
    st = [item.split(' -> ') for item in [con.rstrip('\n') for con in open(txt_name)]]
    print(st)





if __name__ == '__main__':
    solve('test.txt.txt')
