import re

def parse_passport_info(passport_info):
    return dict(x.split(':') for x in passport_info)

def has_all_fields(passport):
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return passport.keys() >= required_keys

def is_valid(passport):
    if not has_all_fields(passport):
        return False
    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return False
    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return False
    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return False

    if passport['hgt'][-2:] == 'cm':
        height = int(passport['hgt'][:-2])
        if height < 150 or height > 193:
            return False
    elif passport['hgt'][-2:] == 'in':
        height = int(passport['hgt'][:-2])
        if height < 59 or height > 76:
            return False
    else:
        return False
    
    if not re.match('^#[0-9a-z]{6}$', passport['hcl']):
        return False
    if not passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not re.match('^[0-9]{9}$', passport['pid']):
        return False

    return True

def main():
    passports = []
    with open('input/input4.txt', 'r') as input:
        passport_info = []
        for line in input:
            if line == '\n':
                passports.append(parse_passport_info(passport_info))
                passport_info = []
            else:
                passport_info += line.strip().split()
        passports.append(parse_passport_info(passport_info))

    part1 = 0
    part2 = 0
    for passport in passports:
        if has_all_fields(passport):
            part1 += 1
        if is_valid(passport):
            part2 += 1
        
    print("Part 1 answer: ", part1)
    print("Part 2 answer: ", part2)

if __name__ == "__main__":
    main()