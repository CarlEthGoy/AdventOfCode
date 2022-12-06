day = 1 # Fill the day number here

with open(f'./data/day{day}.txt', 'r') as data:
  l = [x for x in data]

answer1 = ''
answer2 = ''


print(f'--- Day {day} ---')
print(f'  Part 1 : {answer1}')
print(f'  Part 2 : {answer2}')