day = 1 # Fill the day number here

with open(f'./data/day{day}.txt', 'r') as data:
  l = [x for x in data]

currentNumber = 0
biggestNumber = 0

for s in l:
  if currentNumber > biggestNumber:
    biggestNumber = currentNumber

  if s == '\n':
    currentNumber = 0
    continue

  if int(s) > 0:
    currentNumber += int(s)

print(f'--- Day {day} ---')
print(f'{biggestNumber}')