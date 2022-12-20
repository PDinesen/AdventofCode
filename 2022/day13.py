from ast import literal_eval


def solve(txt_name):
    st = []
    temp = []
    for item in [contents.rstrip('\n') for contents in open(txt_name)]:
        if item == '':
            st.append(temp)
            temp = []
        else:
            temp.append(literal_eval(item))
    st.append(temp)

    st2 = [literal_eval(item) for item in [contents.rstrip('\n') for contents in open(txt_name)] if item != '']
    st2.append([[2]])
    st2.append([[6]])

    def compare(left, right):
        if isinstance(left, list) and isinstance(right, list):
            if len(left) == 0 and len(right) != 0:
                return True
            if len(right) == 0 and len(left) != 0:
                return False
            if len(left) + len(right) == 0:
                return 'fine'
            for num in range(min(len(left), len(right))):
                test = compare(left[num], right[num])
                if test != 'fine':
                    return test
            if len(left) > len(right):
                return False
            elif len(left) < len(right):
                return True
        elif isinstance(left, list) and isinstance(right, int):
            return compare(left, [right])
        elif isinstance(right, list) and isinstance(left, int):
            return compare([left], right)
        else:
            if left == right:
                return 'fine'
            else:
                return left < right

        return 'fine'

    ans = 0
    for i in range(len(st)):
        order = compare(st[i][0], st[i][1])
        if order:
            ans += i + 1
    print(ans)

    ordered = [st2.pop()]
    while len(st2) > 0:
        check = st2.pop()
        for i in range(len(ordered)):
            if not compare(ordered[i], check):
                ordered.insert(i, check)
                break
        if check not in ordered:
            ordered.append(check)
    print((ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1))


if __name__ == '__main__':
    solve('day13.txt')
