# https://adventofcode.com/2022/day/9

file = open("input.txt", "r")
input = file.read()
movements = input.strip().split('\n')

def sign(num):
  return bool(num > 0) - bool(num < 0)

def calculateTailMovement(headPos, tailPos):
  verticalDiff = headPos[1] - tailPos[1]
  horizontalDiff = headPos[0] - tailPos[0]
  if abs(verticalDiff) > 1 and not horizontalDiff:
    return (0, sign(verticalDiff))
  elif abs(horizontalDiff) > 1 and not verticalDiff:
    return (sign(horizontalDiff), 0)
  elif (abs(verticalDiff) > 1 and horizontalDiff) or (abs(horizontalDiff) > 1 and verticalDiff):
    return (sign(horizontalDiff), sign(verticalDiff))
  else:
    return (0,0)

def movePointer(initial, final):
  return tuple(map(sum, zip(initial, final)))

directionalInput = {
  'R': (1,0),
  'L': (-1,0),
  'U': (0,1),
  'D': (0,-1)
}

knotPositions = [(0,0)]*10
visited = set((0,0))

for movement in movements:
  move = movement.split(' ')
  direction = directionalInput[move[0]]
  for enum in range(int(move[1])):
    knotPositions[0] = movePointer(knotPositions[0], direction)
    for i in range(0, len(knotPositions)-1):
      newMovement = calculateTailMovement(knotPositions[i], knotPositions[i+1])
      knotPositions[i+1] = movePointer(knotPositions[i+1], newMovement)
      if i+1 == 9:
        visited.add(knotPositions[i+1])

print(len(visited)-1)
