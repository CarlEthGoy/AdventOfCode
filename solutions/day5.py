from textwrap import wrap

day = 5  # Fill the day number here

with open(f'./data/day{day}.txt', 'r') as filedatas:
    datas = [x for x in filedatas]

sFinal = [[], [], [], [], [], [], [], [], []]
sFinal2 = [[], [], [], [], [], [], [], [], []]
answer1 = ''
answer2 = ''

instructions = []
stacks = []

for data in datas:
    if data.count("move") > 0:
        dataTrimmed = data.replace('move', '').replace('from', '').replace('to', '').replace('\n', '')
        instructions.append(dataTrimmed.split())
    elif data.count("[") > 0:
        dataTrimmed = data.replace('\n', '')
        n = 4
        stacks.append(list([dataTrimmed[i:i+n] for i in range(0, len(dataTrimmed), n)]))

for stack in stacks:
    for s in range(0, len(stack)):
        value = stack[s].replace('[', '').replace(']', '').replace(' ', '')
        if value == '':
            continue

        sFinal[s].append(value)
        sFinal2[s].append(value)

#part1
for instruction in instructions:
    takeX = int(instruction[0])
    fromRow = int(instruction[1])
    toRow = int(instruction[2])

    toMove = sFinal[fromRow - 1][:takeX]
    moveTo = sFinal[toRow - 1]

    for i in toMove:
        sFinal[toRow - 1] = list(i) + sFinal[toRow - 1]
        sFinal[fromRow - 1].remove(i)
for s in sFinal:
    if len(s) > 0:
        answer1 += s[0]

#part2
for instruction in instructions:
    takeX = int(instruction[0])
    fromRow = int(instruction[1])
    toRow = int(instruction[2])

    toMove = sFinal2[fromRow - 1][:takeX][::-1]
    moveTo = sFinal2[toRow - 1]

    for i in toMove:
        sFinal2[toRow - 1] = list(i) + sFinal2[toRow - 1]
        sFinal2[fromRow - 1].remove(i)

for s in sFinal2:
    if len(s) > 0:
        answer2 += s[0]


print(f'--- Day {day} ---')
print(f'p1: {answer1}')
print(f'p2: {answer2}')