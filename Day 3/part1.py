# https://adventofcode.com/2022/day/3

file = open("input.txt", "r")
results = file.read()
rucksacks = results.strip().split('\n')

score = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def findDup(items):
  size = int(len(items)/2)
  first = items[0:size]
  second = items[size:]
  single = [x for x in set(first) if x in set(second)][0]
  return score.index(single) + 1

print(sum(map(findDup, rucksacks)))