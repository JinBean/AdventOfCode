file = open("input.txt", "r")
results = file.read()
rucksacks = results.strip().split('\n')

score = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def findDup(itemArr):
  first = [x for x in set(itemArr[0]) if x in set(itemArr[1])]
  second = [x for x in first if x in set(itemArr[2])][0]
  return score.index(second) + 1

total = 0
for i in range(0, len(rucksacks), 3):
  dup = findDup(rucksacks[i:i+3])
  total += dup
print(total)