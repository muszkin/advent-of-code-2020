import re


def get_passport_data(passport_raw: str):
    passport_raw = passport_raw.replace(" ", "\n")
    data = passport_raw.split("\n")
    passport_data = {}
    for row in data:
        i = row.split(":")
        passport_data[i[0]] = i[1]
    return passport_data


def is_valid_passport(passport_data: dict):
    return "byr" in passport_data and byr_valid(int(passport_data["byr"])) \
           and "iyr" in passport_data and iyr_valid(int(passport_data["iyr"])) \
           and "eyr" in passport_data and eyr_valid(int(passport_data["eyr"])) \
           and "hgt" in passport_data and hgt_valid(passport_data["hgt"]) \
           and "hcl" in passport_data and hcl_valid(passport_data["hcl"]) \
           and "ecl" in passport_data and ecl_valid(passport_data["ecl"]) \
           and "pid" in passport_data and pid_valid(passport_data["pid"])


def byr_valid(byr: int):
    return 1920 <= byr <= 2002


def iyr_valid(iyr: int):
    return 2010 <= iyr <= 2020


def eyr_valid(eyr: int):
    return 2020 <= eyr <= 2030


def hgt_valid(hgt: str):
    metric = hgt[-2:]
    value = hgt[0:-2]
    if re.compile("^\d+$").match(value):
        value = int(value)
        if metric == "in":
            return 59 <= value <= 76
        elif metric == "cm":
            return 150 <= value <= 193
        else:
            return False
    else:
        return False


def hcl_valid(hcl: str):
    return re.compile("^#[0-9a-f]{6}$").match(hcl)


def ecl_valid(ecl: str):
    valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in valid_ecl


def pid_valid(pid: str):
    return re.compile("^\d{9}$").match(pid)


file = open('day4-input.txt', 'r')
passports = file.read().split("\n\n")
valid = 0
for passport in passports:
    if is_valid_passport(get_passport_data(passport)):
        valid += 1

print(valid)
