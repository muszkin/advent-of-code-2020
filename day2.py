def validate1(min, max, letter, password):
    return min <= password.count(letter) <= max

def validate2(pos1, pos2, letter, password):
    return (password[pos1] == letter and password[pos2] != letter) or (password[pos1] != letter and password[pos2] == letter)

file = open('day2-input.txt', 'r')

passwords = file.read().split('\n')

valid1 = 0
valid2 = 0

for password in passwords:
    data = password.split(':')
    info = data[0].split(' ')
    min = info[0].split('-')[0]
    max = info[0].split('-')[1]
    letter = info[1]
    passToCheck = data[1].strip()
    if validate1(int(min), int(max), letter, passToCheck):
        valid1 += 1
    if validate2(int(min) - 1, int(max) - 1, letter, passToCheck):
        valid2 += 1

print(valid1)
print(valid2)
