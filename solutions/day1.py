day = 1  # Fill the day number here

with open(f'./data/day{day}.txt', 'r') as filedatas:
    datas = [x for x in filedatas]

currentNumber = 0
biggestNumber = 0

for data in datas:
    if currentNumber > biggestNumber:
        biggestNumber = currentNumber

    if data == '\n':
        currentNumber = 0
        continue

    if int(data) > 0:
        currentNumber += int(data)

print(f'--- Day {day} ---')
print(f'{biggestNumber}')