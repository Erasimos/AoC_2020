import ut


def get_passports():
    passport_data = [line.split() for line in ut.read_input().split("\n\n")]
    passports = []
    for passport in passport_data:
        new_passport = {}
        for data in passport:
            data = data.split(":")
            new_passport[data[0]] = data[1]
        passports.append(new_passport)
    return passports


def valid_byr(yr):
    return str.isnumeric(yr) and len(yr) == 4 and 1920 <= int(yr) <= 2002


def valid_iyr(yr):
    return str.isnumeric(yr) and len(yr) == 4 and 2010 <= int(yr) <= 2020


def valid_eyr(yr):
    return str.isnumeric(yr) and len(yr) == 4 and 2020 <= int(yr) <= 2030


def valid_hgt(hgt):
    unit = hgt[-2:]
    length = hgt[0:-2]
    if unit == "cm":
        return str.isnumeric(length) and 150 <= int(length) <= 193
    elif unit == "in":
        return str.isnumeric(length) and 59 <= int(length) <= 76
    return False


def valid_hcl(hcl):
    if len(hcl) == 7:
        try:
            color = int(hcl[1:], 16)
            return True
        except ValueError:
            return False
    return False


def valid_ecl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def valid_pid(pid):
    return str.isnumeric(pid) and len(pid) == 9


def valid_cid(cid):
    return True


def is_valid(passport: dict):
    if len(passport) == 7:
        return "cid" not in passport.keys()
    else:
        return len(passport) == 8


validation = {"byr": valid_byr,
              "iyr": valid_iyr,
              "eyr": valid_eyr,
              "hgt": valid_hgt,
              "hcl": valid_hcl,
              "ecl": valid_ecl,
              "cid": valid_cid,
              "pid": valid_pid}


def is_valid_v2(passport):
    if is_valid(passport):
        return all([validation[field](passport[field]) for field in passport.keys()])


def part_one():
    passports = get_passports()
    valid_passports = 0
    for passport in passports:
        valid = is_valid(passport)
        if valid:
            valid_passports += 1
    ut.print_answer(valid_passports)


def part_two():
    passports = get_passports()
    valid_passports = 0
    for passport in passports:
        valid = is_valid_v2(passport)
        if valid:
            valid_passports += 1
    ut.print_answer(valid_passports)


part_two()

