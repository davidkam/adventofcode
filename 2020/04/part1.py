required_keys = [
  'byr',
  'iyr',
  'eyr',
  'hgt',
  'hcl',
  'ecl',
  'pid'
]

optional_keys = [
  'cid'
]

def checkValid(passport_data):
    valid = False
    checksum = 0
    passport = ' '.join(passport_data)
    passport_elements = passport.split(' ')
    for element in passport_elements:
        [key,value] = element.split(':')
        if key in required_keys:
            checksum += 1
    valid = True if checksum >=7 else False
    return 1 if valid else 0

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


print(num_valid)
