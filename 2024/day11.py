from functools import wraps

for item in [contents.rstrip('\n') for contents in open('input/' + 'day11' + '.txt')]:
    st = item.split(' ')
##st = ['125', '17']
##print(st)




def blink(stone):
    if stone == '0':
        return ['1']
    elif len(stone) % 2 == 0:
        return [str(int(stone[:len(stone)//2])), str(int(stone[len(stone)//2:]))]
    else:
        return [str(int(stone) * 2024)]


test = ['0', '1', '10']
print(test)
for el in test:
    print(blink(el))

track = dict()

not_continue = []

def run(times, stones):
    temp = stones
    for i in range(times):
        new = []
        for el in temp:
            for el2 in blink(el):
                new.append(el2)
        temp = new
    print(len(temp))

run(25, st)



def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]
    return wrapper


@memoize
def count_stones(stone, blinks):
    if blinks == 0:
        return 1
    return sum(count_stones(s, blinks - 1) for s in blink(stone))

print(sum(count_stones(stone, 75) for stone in st))