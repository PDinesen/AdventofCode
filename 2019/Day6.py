filename = 'test'

data = [line.rstrip('\n').split(')') for line in open(filename)]

print(data)

def run(input_data):
    res =