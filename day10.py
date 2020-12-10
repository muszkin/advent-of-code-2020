jolts = [0] + sorted([int(x) for x in open("day10-input.txt").readlines()])


def get_next(jolt: int, diff_one=0, diff_two=0, diff_three=0):
    search = jolt + 1
    if search in jolts:
        diff_one += 1
    else:
        search += 1
        if search in jolts:
            diff_two += 1
        else:
            search += 1
            if search in jolts:
                diff_three += 1
            else:
                return diff_one, diff_two, diff_three
    return get_next(search, diff_one, diff_two, diff_three)


diff_1, diff_2, diff_3 = get_next(0, diff_three=1)

print(diff_1 * diff_3)

ways_count = [1] + [0 for x in range(len(jolts) - 1)]
for x in range(len(jolts)):
    for y in range(1, 4):
        if jolts[x] + y in jolts:
            ways_count[jolts.index(jolts[x] + y)] += ways_count[x]

print(ways_count[-1])
