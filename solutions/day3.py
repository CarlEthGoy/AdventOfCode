day = 3 # Fill the day number here

with open(f'./data/day{day}.txt', 'r') as filedatas:
    datas = [x for x in filedatas]

sumOfPriorities = 0

def GetValueInPoints(item):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96

# part1
for data in datas:
    #split data in two
    firstRucksack = list(data[:int(len(data)/2)])
    secondRucksack = list(data[int(len(data)/2):])

    #find the occurence of the same char, respect uper and lower
    item = list(set(firstRucksack).intersection(secondRucksack))[0]
    sumOfPriorities += GetValueInPoints(item)

# part2
firstRucksack = []
secondRucksack = []
thirdRucksack = []
index = 0
sumOfPriorities2 = 0

for data in datas:
    data = data.replace('\n', '')
    if index == 0:
        firstRucksack = data
        index += 1
    elif index == 1:
        secondRucksack = data
        index += 1
    else:
        thirdRucksack = data
        item = list(set(firstRucksack).intersection(secondRucksack).intersection(thirdRucksack))[0]
        sumOfPriorities2 += GetValueInPoints(item)
        index = 0

print(firstRucksack)
print(secondRucksack)
print(thirdRucksack)
item = list(set(firstRucksack).intersection(secondRucksack).intersection(thirdRucksack))[0]
print(item)




print(f'--- Day {day} ---')
print(f'{sumOfPriorities}')
print(f'{sumOfPriorities2}')