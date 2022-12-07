day = 1  # Fill the day number here

with open(f'./data/day{day}.txt', 'r') as filedatas:
    datas = [x for x in filedatas]

currentNumber = 0
maximumCalories = 0
maximumCaloriesArr = []

for data in datas:
    if currentNumber > maximumCalories:
        maximumCalories = currentNumber

    if data == '\n':
        maximumCaloriesArr.append(currentNumber)
        currentNumber = 0
        continue

    if int(data) > 0:
        currentNumber += int(data)

maximumCaloriesTop3 = sum(sorted(maximumCaloriesArr)[-3:])

print(f'--- Day {day} ---')
print(f'p1: {maximumCalories}')
print(f'p2: {maximumCaloriesTop3}')
