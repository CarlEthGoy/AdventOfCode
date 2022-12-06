day = 1 # Fill the day number here

with open(f'./data/day{day}.txt', 'r') as filedatas:
    datas = [x for x in filedatas]

answer1 = ''
answer2 = ''


print(f'--- Day {day} ---')
print(f'  Part 1 : {answer1}')
print(f'  Part 2 : {answer2}')