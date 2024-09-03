f = open("input.txt", "r")
data = f.read().split("\n")
data.pop()

winners = []
for line in data:
  (game_info,card_data) = line.split(':')
  (raw_winning_numbers, raw_my_numbers) = card_data.split('|')
  winning_numbers = raw_winning_numbers.split()
  my_numbers = raw_my_numbers.split()
  print(winning_numbers,my_numbers)
  cnt = 0
  for winning_number in winning_numbers:
    if winning_number in my_numbers:
      cnt += 1
  winners.append(cnt)


sum = 0
for cnt in winners:
  if cnt:
    sum += 2 ** (cnt - 1)

print(sum)
