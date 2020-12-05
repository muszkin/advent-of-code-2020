def get(seat_row: str, ran: list):
    for index, sr in enumerate(seat_row):
        if index == len(seat_row) - 1:
            if sr == "F" or sr == "L":
                return ran[0]
            else:
                return ran[1]
        if sr == "F" or sr == "L":
            ran = ran[0:int(len(ran)/2)]
        else:
            ran = ran[int(len(ran)/2):]


file = open("day5-input.txt", "r")

seats = map(str, file.read().split("\n"))

ids = []

for seat in seats:
    row = get(seat[0:7], list(range(0, 128)))
    column = get(seat[7:], list(range(0, 8)))
    ids.append(row * 8 + column)

print(max(ids))

for i in ids:
    if i + 2 in ids and i + 1 not in ids:
        print(i + 1)
