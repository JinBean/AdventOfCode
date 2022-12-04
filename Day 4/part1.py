# https://adventofcode.com/2022/day/4

file = open("input.txt", "r")
results = file.read()
assignments = results.strip().split('\n')



def findOverlap(pairs):
  ranges = pairs.replace('-', ',').split(',')
  intranges = [int(i) for i in ranges]
  if ((intranges[0] >= intranges[2] and intranges[1] <= intranges[3]) or (intranges[2] >= intranges[0] and intranges[3] <= intranges[1])):
    return 1
  return 0

print(sum(map(findOverlap, assignments)))
