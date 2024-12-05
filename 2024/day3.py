import re

st1 = [item for item in [contents for contents in open('input/' + 'day3' + '.txt')]]
st = ''
for s in st1:
    st += s
print(st)


match = r"mul\((\d{1,3},\d{1,3})\)"
matches = re.findall(match, st)

print(matches)

p = 0

for mul in matches:
    n = mul.split(',')
    p += int(n[0]) * int(n[1])

print(p)

do = "do()"
dont = "don't()"

m2 = []
stop = st.find(dont)
temp = st
while stop != -1:
    for x in re.findall(match, temp[: stop]):
        m2.append(x)
    temp = temp[stop:]
    print(stop, temp.find(do))
    temp = temp[temp.find(do):]
    print(len(temp))
    print(temp[:4])
    stop = temp.find(dont)

p2 = 0
for mul in m2:
    n = mul.split(',')
    p2 += int(n[0]) * int(n[1])

print(p2)


