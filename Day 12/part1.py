# https://adventofcode.com/2022/day/12

with open("input.txt", "r") as file:
  input = file.read()
  combinedString = input.replace('\n', '')
  heightMap = input.strip().split('\n')

global heightRange
heightRange = 'abcdefghijklmnopqrstuvwxyz'

startPos = combinedString.index('S')
startPosYX = (startPos//len(heightMap[0]), startPos%len(heightMap[0]))
endPos = combinedString.index('E')
endPosYX = (endPos//(len(heightMap[0])), endPos%(len(heightMap[0])))

heightMap = [h.replace('S', 'a').replace('E', 'z') for h in heightMap]

def evaluatePos(pos):
  possiblePaths = []
  y, x = pos
  height = heightRange.index(heightMap[y][x])
  range = heightRange[:min(25, height+1) + 1]
  possiblePos = [(y, min(len(heightMap[0])-1, x+1)), (y, max(x-1, 0)), (max(0, y-1), x), (min(len(heightMap)-1, y+1), x)]
  for i in possiblePos:
    iy, ix = i
    value = heightMap[iy][ix]
    if value in range:
      possiblePaths.append((iy, ix))
  return possiblePaths

pathMatrix = [[0]*len(heightMap[0]) for i in range(len(heightMap))]
pathMatrix[startPosYX[0]][startPosYX[1]] = 1

## BFS
def calculateSteps(steps):
  for i in range(len(heightMap)):
    for j in range(len(heightMap[0])):
      if pathMatrix[i][j] == steps:
        possiblePaths = evaluatePos((i,j))
        for path in possiblePaths:
          if pathMatrix[path[0]][path[1]] == 0:
            pathMatrix[path[0]][path[1]] = steps + 1

def bfs():
  steps = 0
  while pathMatrix[endPosYX[0]][endPosYX[1]] == 0:
      steps += 1
      calculateSteps(steps)
  print(steps)

bfs()
