file = open("input.txt", "r")
results = file.read()
assignments = results.strip().split('\n')



def findOverlap(pairs):
  ranges = pairs.replace('-', ',').split(',')
  intranges = [int(i) for i in ranges]
  if ((intranges[1] < intranges[2]) or (intranges[0] > intranges[3])):
    return 0
  return 1

print(sum(map(findOverlap, assignments)))
