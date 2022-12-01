def solve(txt_name):
    st = [item for item in [contents.rstrip('\n') for contents in open(txt_name)]]
    st2 = []
    temp = 0
    for item in st:
        if item == "":
            st2.append(temp)
            temp = 0
        else:
            temp += int(item)
    st = st2
    temp = 0
    for i in range(3):
        temp += max(st)
        st.remove(max(st))
    return max(st2), temp


if __name__ == "__main__":
    print(solve("day1.txt"))
