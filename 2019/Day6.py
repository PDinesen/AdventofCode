filename = 'test'

data = [line.rstrip('\n').split(')') for line in open(filename)]

print(data)

def run(input_list):
    planets = {}
    for item in input_list:
        if item[0] in