day = 2  # Fill the day number here

with open(f'./data/day{day}.txt', 'r') as filedatas:
    datas = [x for x in filedatas]

elfDic = {'Rock': 'A', 'Paper': 'B', 'Scissors': 'C'}
myDic = {'Rock': 'X', 'Paper': 'Y', 'Scissors': 'Z'}
pointsValue = {'X': 1, 'Y': 2, 'Z': 3}
gameValue = {'win': 6, 'lose': 0, 'tie': 3}
points = 0

for data in datas:
    elfPick = data[0]
    myPick = data[2]
    points += pointsValue[myPick]

    if list(elfDic.values()).index(elfPick) == list(myDic.values()).index(myPick):
        points += gameValue['tie']
    elif elfPick == elfDic['Scissors'] and myPick == myDic['Rock'] \
            or elfPick == elfDic['Paper'] and myPick == myDic['Scissors'] \
            or elfPick == elfDic['Rock'] and myPick == myDic['Paper']:
        points += gameValue['win']
    else:
        points += gameValue['lose']

print(f'--- Day {day} ---')
print(points)
