day = 4 # Fill the day number here

with open(f'./data/day{day}.txt', 'r') as filedatas:
    datas = [x for x in filedatas]


def get_is_overlapping_by_x(data, x):
    ranges = data.replace('\n', '').split(',')
    range1 = ranges[0].split('-')
    range2 = ranges[1].split('-')

    r1 = []
    r2 = []
    for i in range(int(range1[0]), int(range1[1])+1):
        r1.append(i)

    for i in range(int(range2[0]), int(range2[1])+1):
        r2.append(i)

    return len(list(set(r1).intersection(r2))) > x


# part1
overlapCount = 0
for data in datas:
    isOverlapping = get_is_overlapping_by_x(data, 2)
    if isOverlapping:
        overlapCount += 1

# part2
overlapCount2 = 0
for data in datas:
    isOverlapping = get_is_overlapping_by_x(data, 0)

    if isOverlapping:
        overlapCount2 += 1

print(f'--- Day {day} ---')
print(f'p1: {overlapCount}')
print(f'p2: {overlapCount2}')