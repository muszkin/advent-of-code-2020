file = open("day1-input.txt", "r")

numbers = file.read().split("\n")

pair = []

for number in numbers:
    for n in numbers:
        if int(number) + int(n) == 2020 :
            pair.append(int(number))
            pair.append(int(n))
            break
    else:
        continue
    break

print(pair[0] * pair[1])

pair = []

for number in numbers:
    for n in numbers:
        for nu in numbers:
            if int(number) + int(n) + int(nu) == 2020:
                pair.append(int(number))
                pair.append(int(n))
                pair.append(int(nu))


print(pair[0] * pair[1] * pair[2])