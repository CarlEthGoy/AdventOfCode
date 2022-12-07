day = 2  # Fill the day number here

with open(f'./data/day{day}.txt', 'r') as filedatas:
    datas = [x for x in filedatas]

def get_corresponding_value_for_elf_pick():
    return list(ELF_PICK.keys())[list(ELF_PICK.values()).index(elfPick)]


def get_corresponding_value_for_my_pick():
    return list(MY_PICK.keys())[list(MY_PICK.values()).index(myPick)]


ELF_PICK = {'Rock': 'A', 'Paper': 'B', 'Scissors': 'C'}
MY_PICK = {'Rock': 'X', 'Paper': 'Y', 'Scissors': 'Z'}
MY_PICK_2 = {'X': 'lose', 'Y': 'tie', 'Z': 'win'}

PICK_TO_LOSE = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
PICK_TO_WIN = {'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'}

POINTS_VALUE = {'X': 1, 'Y': 2, 'Z': 3}
POINTS_VALUE_2 = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

GAME_VALUE = {'win': 6, 'lose': 0, 'tie': 3}


# part1
pointsPart1 = 0
for data in datas:
    elfPick = data[0]
    myPick = data[2]
    pointsPart1 += POINTS_VALUE[myPick]

    if get_corresponding_value_for_my_pick() == get_corresponding_value_for_elf_pick():
        pointsPart1 += GAME_VALUE['tie']
    elif elfPick == ELF_PICK['Scissors'] and myPick == MY_PICK['Rock'] \
            or elfPick == ELF_PICK['Paper'] and myPick == MY_PICK['Scissors'] \
            or elfPick == ELF_PICK['Rock'] and myPick == MY_PICK['Paper']:
        pointsPart1 += GAME_VALUE['win']
    else:
        pointsPart1 += GAME_VALUE['lose']

# part2
pointsPart2 = 0
for data in datas:
    elfPick = data[0]  # A
    myPick = data[2]  # X

    elfPickValue = get_corresponding_value_for_elf_pick()  # Rock
    whatShouldIDo = MY_PICK_2[myPick]  # lose, tie, win

    whatIWillPlay = ''
    if whatShouldIDo == 'tie':
        whatIWillPlay = elfPickValue
    elif whatShouldIDo == 'lose':
        whatIWillPlay = PICK_TO_LOSE[elfPickValue]
    elif whatShouldIDo == 'win':
        whatIWillPlay = PICK_TO_WIN[elfPickValue]

    pointsPart2 += POINTS_VALUE_2[whatIWillPlay]
    pointsPart2 += GAME_VALUE[whatShouldIDo]


print(f'--- Day {day} ---')
print(f'p1: {pointsPart1}')
print(f'p2: {pointsPart2}')
