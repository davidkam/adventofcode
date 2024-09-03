import re
from collections import OrderedDict 

with open('input.txt', 'r') as f:
  data = f.read().split("\n")

data.pop()
 
def group_list(lst):
    res =  [(el, lst.count(el)) for el in lst]
    return list(OrderedDict(res).items())



ref = {}
hands = {}
rankings = [
  '5K',
  '4K',
  'FH',
  '3K',
  '2P',
  '1P',
  'HC',
]
rep = {
  "A": "F",
  "K": "E",
  "Q": "D",
  "J": "C",
  "T": "B",
}
# use these three lines to do the replacement
for line in data:
  (hand,bid) = line.split(' ')
  rep = dict((re.escape(k), v) for k, v in rep.items()) 
  pattern = re.compile("|".join(rep.keys()))
  shand = pattern.sub(lambda m: rep[re.escape(m.group(0))], hand)
  sorted_hand = sorted(hand)
  shand_key = "".join(sorted_hand)
  info = group_list(sorted_hand)
  hand_type = ''
  if len(info) == 5:
    hand_type = "HC"
  if len(info) == 4:
    hand_type = '1P'
  if len(info) == 3:
    rolls = dict(info)
    if sorted(list(rolls.values()))[2] == 3:
      hand_type = '3K'
    else:
      hand_type = '2P'
  if len(info) == 2:
    rolls = dict(info)
    if sorted(list(rolls.values()))[1] == 3:
      hand_type = 'FH'
    else:
      hand_type = '4K'
  if len(info) == 1:
    hand_type = "5K"  
  if hand_type in hands:
    hands[hand_type].append(shand)
  else:
    hands[hand_type] = [shand]
  ref[shand] = {
    "raw": hand,
    "shand": shand,
    "sorted": sorted_hand,
    "hand_type": hand_type,
    "bid": bid,
  }
  
print(ref)
print(hands)

rankings.reverse()
x = 0
tot = 0
for ranking in rankings:
  if ranking not in hands:
    continue
  sorted_hands = hands[ranking]
  sorted_hands.sort()
  for hand in sorted_hands:
    x += 1
    bid = int(ref[hand]['bid'])
    tot += (x * bid)
    print(ranking, hand, x, bid, (x * bid), tot)


print(tot)
