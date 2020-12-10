import re

valid_ecl = [
    'amb',
    'blu',
    'brn',
    'gry',
    'grn',
    'hzl',
    'oth'
]

def eclValidate(val):
    return True if val in valid_ecl else False

def byrValidate(val):
    try:
        return True if int(val) >= 1920 and int(val) <= 2002 else False
    except:
        return False

def iyrValidate(val):
    try:
        return True if int(val) >= 2010 and int(val) <= 2020 else False
    except:
        return False

def eyrValidate(val):
    try:
        return True if int(val) >= 2020 and int(val) <= 2030 else False
    except:
        return False

def hgtValidate(val):
    valid = False
    uom = val[-2:]
    if uom == "cm":
        val = int(val.replace(uom,""))
        if val >= 150 and val <= 193:
            valid = True
    if uom == "in":
        val = int(val.replace(uom,""))
        if val >= 59 and val <= 76:
            valid = True
    return valid

def hclValidate(val):
    is_hex = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', val)
    return True if is_hex is not None else False

def pidValidate(val):
    is_id = re.search(r'^\d{9}$', val)
    return True if is_id is not None else False

def cidValidate(val):
    return True

functions = {
    'ecl': eclValidate,
    'byr': byrValidate,
    'iyr': iyrValidate,
    'eyr': eyrValidate,
    'hgt': hgtValidate,
    'hcl': hclValidate,
    'pid': pidValidate,
    'cid': cidValidate
}
def checkValid(passport_data):
    passport_dict = {}
    passport = ' '.join(passport_data)
    passport_elements = passport.split(' ')
    for element in passport_elements:
        [key,value] = element.split(':')
        passport_dict[key] = value
    for key in functions:
        if key in passport_dict:
            value = passport_dict[key]
            if not functions[key](value):
                return 0
        else:
            if key != 'cid':
                return 0
    return 1

f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()
num_valid = 0
id_data = []
for line in data:
    if line == '':
        num_valid += checkValid(id_data)
        id_data = []
        continue
    id_data.append(line)
num_valid += checkValid(id_data)
print(num_valid)
