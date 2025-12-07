st = [item for item in [content.rstrip('\n') for content in open('day7.txt')]]

splits = 0
beamPosition = {st[0].index('S'): 1}
splitterPositions = []
for row in st:
    splitters = [i for i in range(len(row)) if row[i] == '^']
    if splitters:
        splitterPositions.append(splitters)

for s in splitterPositions:
    temp = {}
    for b in beamPosition.keys():
        if b in s:
            if b - 1 not in temp.keys():
                temp[b - 1] = beamPosition[b]
            else:
                temp[b - 1] += beamPosition[b]
            if b + 1 not in temp.keys():
                temp[b + 1] = beamPosition[b]
            else:
                temp[b + 1] += beamPosition[b]
            splits += 1
        else:
            if b not in temp.keys():
                temp[b] = beamPosition[b]
            else:
                temp[b] += beamPosition[b]
    beamPosition = temp

print(splits)
print(sum(beamPosition.values()))
