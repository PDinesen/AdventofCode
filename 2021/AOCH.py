def ril(filename):
    return [line.rstrip('\n') for line in open(filename)]
