v = 1001
print(int(str(v)[1]))


def repeating(number):
    s = str(number)
    for letter in s:
        if s.count(letter) == 2:
            return True
    return False


def repeatstop(number):
    s = str(number)
    for letter in s:
        if s.count(letter) > 2:
            return False
    return True


def degrees(number):
    s = str(number)
    prev = 0
    for letter in s:
        if int(letter) < prev:
            return False
        else:
            prev = int(letter)
    return True


def run(low, high):
    count = 0
    for i in range(low, high+1):
        if degrees(i) and repeating(i):
            count += 1
    return count


print(run(284639, 748759))
