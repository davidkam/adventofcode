f = open("input.txt", "r")
data = f.read().split("\n")
data.pop()

winners = {}
for x in range(len(data)):
  winners[x + 1] = 1


for x in range(len(data)):
  line = data[x]
  (game_info,card_data) = line.split(':')
  card_number = int(game_info.replace('Card ',''))
  multiplier = winners[card_number]
  print('m', multiplier)
  (raw_winning_numbers, raw_my_numbers) = card_data.split('|')
  winning_numbers = raw_winning_numbers.split()
  my_numbers = raw_my_numbers.split()
  cnt = 0
  for winning_number in winning_numbers:
    if winning_number in my_numbers:
      cnt += 1
  for step in range(cnt):
    key = card_number + 1 + step
    print('k', key)
    if key in winners:
      winners[key] += multiplier
    else:
      winners[key] = 1
  print(winners)


print(sum(list(winners.values())))
