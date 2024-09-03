f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

ref = {
  'red': 12,
  'green': 13,
  'blue': 14,
}

num = 0
for line in data:
  print(line)
  (game_info, games) = line.split(': ')
  game_no = game_info.replace('Game ','')
  grabs = games.split('; ')
  min = {} 
  for grab in grabs:
    rolls = grab.split(', ')
    for roll in rolls:
      for color in ref.keys():
        if color in roll:
          check_num = int(roll.replace(' ' + color, ''))
          if color not in min:
            min[color] = check_num
          else:
            if check_num > min[color]:
              min[color] = check_num
           
  mult = 1
  print(min)
  for power in list(min.values()):
    mult *= power

  print(mult)

  num += mult
print(num)
