from functools import reduce

file = open('day3-input.txt', 'r')
whole_map = file.read().split("\n")

trees = 0
result = 0

slopeRun = []


def get_next_position(pos, record):
    max_len = len(record) - 1
    if pos > max_len:
        pos -= len(record)
    return pos


def get_next_row(all_rows, down, current):
    max_row = len(all_rows) - down
    if current + down > max_row:
        return False
    return current + down


slopeDir = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
position = 0

for index, row in enumerate(whole_map):
    max_index = len(whole_map) - 1
    if index < max_index:
        position = get_next_position(position + 3, row)
        if whole_map[index + 1][position] == "#":
            trees += 1

print(trees)

trees = 0
currentRow = 0
for slope in slopeDir:
    position = 0
    for x in range(0, int(len(whole_map)/slope[1]), 1):
        currentRow = get_next_row(whole_map, slope[1], currentRow)
        if currentRow and isinstance(currentRow, int):
            position = get_next_position(position + slope[0], whole_map[currentRow])
            if whole_map[currentRow][position] == "#":
                trees += 1
    slopeRun.append(trees)
    trees = 0

print(reduce(lambda a, b: a * b, slopeRun))
