f = open("input.txt", "r")
data = f.read().split("\n")
data.pop()

numbers_keys = {
  'one': 'o1e',
  'two': 't2o',
  'three': 't3e',
  'four': 'f4r',
  'five': 'f5e',
  'six': 's6x',
  'seven': 's7n',
  'eight': 'e8t',
  'nine': 'n9e',
}

def get_num(letters):
  for letter in letters:
    if letter.isdigit():
      return letter

def convert_nums(line):
  for key in numbers_keys.keys():
    line = line.replace(key, str(numbers_keys[key]))
  return line

sum = 0
for line in data:
  left_num = get_num(convert_nums(line))
  right_num = get_num(reversed(convert_nums(line)))
  num = left_num + right_num
  sum += int(num)

print(sum)
