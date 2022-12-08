day = 6  # Fill the day number here

with open(f'./data/day{day}.txt', 'r') as filedatas:
    datas = [x for x in filedatas]

DISTINCT_CHARS_PACKET = 4
DISTINCT_CHARS_MESSAGE = 14

answer1 = 0
answer2 = 0

serie = ""
# part1
data = datas[0]
for i in range(0, len(data)):
    serie += data[i]
    indexOf = serie.index(data[i])
    if serie.count(data[i]) > 1:
        serie = serie[indexOf+1:]

    if len(serie) == DISTINCT_CHARS_PACKET:
        answer1 = i + 1
        break

# part1
data = datas[0]
for i in range(0, len(data)):
    serie += data[i]
    indexOf = serie.index(data[i])
    if serie.count(data[i]) > 1:
        serie = serie[indexOf+1:]

    if len(serie) == DISTINCT_CHARS_MESSAGE:
        answer2 = i + 1
        break

print(f'--- Day {day} ---')
print(f'p1: {answer1}')
print(f'p2: {answer2}')