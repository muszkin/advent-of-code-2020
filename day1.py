file = open("day1-input.txt", "r")

numbers = file.read().split("\n")

pair = []

for index, number in enumerate(numbers):
    for n in numbers[index:]:
        if number != n:
            if int(number) + int(n) == 2020:
                pair.append(int(number))
                pair.append(int(n))
                break
    else:
        continue
    break

print(pair[0] * pair[1])

pair = []

for index, number in enumerate(numbers):
    for i, n in enumerate(numbers[index:]):
        if n != number:
            for nu in numbers[i:]:
                if nu != number and n != number and nu != n:
                    if int(number) + int(n) + int(nu) == 2020:
                        pair.append(int(number))
                        pair.append(int(n))
                        pair.append(int(nu))


print(pair[0] * pair[1] * pair[2])