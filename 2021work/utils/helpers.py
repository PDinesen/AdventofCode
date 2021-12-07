from functools import wraps


def to_hashable(*args, **kwargs):
    if len(kwargs) > 0:
        return to_hashable(*args, *kwargs.items())
    assert len(args) > 0
    if len(args) == 1:
        arg = args[0]
        if isinstance(arg, list):
            return tuple(to_hashable(a) for a in arg),
        elif isinstance(arg, set):
            return tuple(a for a in sorted(arg, key=hash)),
        elif isinstance(arg, dict):
            return to_hashable(*arg.items()),
        elif isinstance(arg, tuple):
            return arg,
        return arg
    return tuple(to_hashable(arg) for arg in args)


def memoize(f):
    mem = {}

    @wraps(f)
    def inner(*args, **kwargs):
        key = to_hashable(*args, **kwargs)
        if key in mem:
            return mem[key]
        result = f(*args, **kwargs)
        mem[key] = result
        return mem[key]

    return inner


if __name__ == '__main__':
    print(to_hashable(1))
    print(to_hashable([1, 2, 3]))
    print(to_hashable((1, 2)))
    print(to_hashable(1, 2))
    print(to_hashable({1, 2, 'a'}))
    print(to_hashable({'a': [1, 2]}))
    print(to_hashable({'a': 'b'}))
    print(to_hashable({'a': 'b', 'c': 'd'}, 1))