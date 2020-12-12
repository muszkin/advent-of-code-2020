import copy

data = open('day11-input.txt', 'r').read().split('\n')

seats = [['X' for x in range(len(data[0]) + 2)]]
for line in data:
    line = 'X' + line + 'X'
    seats.append(list(line))
seats.append(['X' for x in range(len(seats[0]))])


def check_tl(l, i, j, start=False):
    if l[i][j] == 'X' and not start:
        return 0
    if l[i][j] == '#' and not start:
        return 1
    if l[i][j] == 'L' and not start:
        return 0
    return check_tl(l, i - 1, j - 1)


def check_t(l, i, j, start=False):
    if l[i][j] == 'X' or l[i][j] == 'L' and not start:
        return 0
    if l[i][j] == '#' and not start:
        return 1
    return check_t(l, i - 1, j)


def check_tr(l, i, j, start=False):
    if l[i][j] == 'X' or l[i][j] == 'L' and not start:
        return 0
    if l[i][j] == '#' and not start:
        return 1
    return check_tr(l, i - 1, j + 1)


def check_ml(l, i, j, start=False):
    if l[i][j] == 'X' or l[i][j] == 'L' and not start:
        return 0
    if l[i][j] == '#' and not start:
        return 1
    return check_ml(l, i, j - 1)


def check_mr(l, i, j, start=False):
    if l[i][j] == 'X' or l[i][j] == 'L' and not start:
        return 0
    if l[i][j] == '#' and not start:
        return 1
    return check_mr(l, i, j + 1)


def check_bl(l, i, j, start=False):
    if l[i][j] == 'X' or l[i][j] == 'L' and not start:
        return 0
    if l[i][j] == '#' and not start:
        return 1
    return check_bl(l, i + 1, j - 1)


def check_b(l, i, j, start=False):
    if l[i][j] == 'X' or l[i][j] == 'L' and not start:
        return 0
    if l[i][j] == '#' and not start:
        return 1
    return check_b(l, i + 1, j)


def check_br(l, i, j, start=False):
    if l[i][j] == 'X' or l[i][j] == 'L' and not start:
        return 0
    if l[i][j] == '#' and not start:
        return 1
    return check_br(l, i + 1, j + 1)


swap = True
while swap:
    swap = False
    cpy = copy.deepcopy(seats)
    for i in range(1, len(seats) - 1):
        for j in range(1, len(seats[i]) - 1):
            if seats[i][j] == 'L':
                if check_tl(cpy, i, j, True) + check_t(cpy, i, j, True) + check_tr(cpy, i, j, True) + check_ml(cpy, i,
                                                                                                               j,
                                                                                                               True) + \
                        check_mr(cpy, i, j, True) + check_bl(cpy, i, j, True) + check_b(cpy, i, j, True) + check_br(cpy,
                                                                                                                    i,
                                                                                                                    j,
                                                                                                                    True) == 0:
                    seats[i][j] = '#'
                    swap = True
            elif seats[i][j] == '#':
                if check_tl(cpy, i, j, True) + check_t(cpy, i, j, True) + check_tr(cpy, i, j, True) + check_ml(cpy, i,
                                                                                                               j,
                                                                                                               True) + \
                        check_mr(cpy, i, j, True) + check_bl(cpy, i, j, True) + check_b(cpy, i, j, True) + check_br(cpy,
                                                                                                                    i,
                                                                                                                    j,
                                                                                                                    True) > 4:
                    seats[i][j] = 'L'
                    swap = True

seated = 0
for row in seats:
    for seat in row:
        if seat == '#':
            seated += 1

print(seated)
