f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

def get_left_num(letters):
  for letter in letters:
    if letter.isdigit():
      return letter

def get_right_num(letters):
  for letter in reversed(letters):
    if letter.isdigit():
      return letter


sum = 0
for line in data:
  letters = list(line)
  left_num = get_left_num(letters)
  right_num = get_right_num(letters)
  num = left_num + right_num
  sum += int(num)


print(sum)
