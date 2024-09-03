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
  (game_info, games) = line.split(': ')
  game_no = game_info.replace('Game ','')
  grabs = games.split('; ')
  legit = True
  for grab in grabs:
    rolls = grab.split(', ')
    for roll in rolls:
      for color in ref.keys():
        if color in roll:
          check_num = roll.replace(' ' + color, '')
          if int(check_num) > ref[color]:
            legit = False
  if legit:
    num += int(game_no)


print(num)
