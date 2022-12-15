# https://adventofcode.com/2022/day/14

with open("testinput.txt", "r") as file:
  input = file.read()
  rocks = input.strip().split('\n')

rows, cols = (510, 510)
rockFormation = [[0 for i in range(cols+1)] for j in range(rows+1)]

def formRocks(rockPath):
  straightPaths = rockPath.split(' -> ')
  previousX, previousY = straightPaths[0].split(',')
  previousX, previousY = int(previousX), int(previousY)
  for path in straightPaths:
    currentX, currentY = path.split(',')
    currentX, currentY = int(currentX), int(currentY)

    if currentX < previousX:
      for x in range(currentX, previousX+1):
        rockFormation[currentY][x] = 1
    elif currentX > previousX:
      for x in range(previousX, currentX+1):
        rockFormation[currentY][x] = 1

    if currentY < previousY:
      for y in range(currentY, previousY+1):
        rockFormation[y][currentX] = 1
    elif currentY > previousY:
      for y in range(previousY, currentY+1):
        rockFormation[y][currentX] = 1

    previousX, previousY = currentX, currentY

def dropSand(rockFormation, initialPoint):
  initialX, initialY = initialPoint
  x, y = initialX, initialY
  dropping = True
  finished = False
  while dropping:
    try:
      if not rockFormation[y+1][x]:
        y, x = y+1, x
      elif not rockFormation[y+1][x-1]:
        y, x = y+1, x-1
      elif not rockFormation[y+1][x+1]:
        y, x = y+1, x+1
      else:
        rockFormation[y][x] = 5
        dropping = False
    except IndexError:
      dropping = False
      finished = True
  return rockFormation, finished

for i in rocks:
  formRocks(i)

finished = False
count = 0
while not finished:
  count += 1
  rockFormation, finished = dropSand(rockFormation, (500,0))

print(count-1)


