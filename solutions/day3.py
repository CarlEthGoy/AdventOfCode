day = 3  # Fill the day number here

with open(f'./data/day{day}.txt', 'r') as filedatas:
    datas = [x for x in filedatas]


def get_value_in_points(item):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96


# part1
sumOfPriorities = 0
for data in datas:
    # split data in two
    firstRucksack = list(data[:int(len(data) / 2)])
    secondRucksack = list(data[int(len(data) / 2):])

    # find the occurrence of the same char, respect upper and lower
    item = list(set(firstRucksack).intersection(secondRucksack))[0]
    sumOfPriorities += get_value_in_points(item)

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
        sumOfPriorities2 += get_value_in_points(item)
        index = 0

print(f'--- Day {day} ---')
print(f'{sumOfPriorities}')
print(f'{sumOfPriorities2}')
