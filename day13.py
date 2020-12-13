timetable = open("day13-input.txt", "r").read().split("\n")

timestamp = int(timetable[0])

buses = list(map(int, timetable[1].replace("x,", "").split(",")))

timestamps = dict()

for bus in buses:
    current = 0
    while current < timestamp:
        current += bus
    timestamps[bus] = current

bus_id = sorted(timestamps.items(), key=lambda x: x[1])[0]

print(bus_id[0] * (bus_id[1] - timestamp))

timetable[1] = [i for i in timetable[1].split(',')]


bus_list = [int(i) for i in timetable[1] if i != 'x']

x_count = 0
time_offset_list = []
for item in timetable[1][1:]:
    if item == 'x':
        x_count += 1
    else:
        time_offset_list.append(x_count + 1)
        x_count = 0
time_offset_list.append(1)


def calc(bus, cum_product, offset, timeoffset):
    i = 1
    check = False
    while not check:
        value = i * cum_product + offset - timeoffset
        if value % bus == 0:
            return value, bus * cum_product
        i += 1


offset = 0
cum_product = 1
for i in range(len(bus_list) - 1, -1, -1):
    bus = bus_list[i]
    time_offset = time_offset_list[i]
    offset, cum_product = calc(bus, cum_product, offset, time_offset)

print(offset)