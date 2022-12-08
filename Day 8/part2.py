file = open("input.txt", "r")
input = file.read()
trees = input.strip().split('\n')
trees = [[x for x in i] for i in trees]


def findScore(treePosition):
  left = right = top = bottom = 0
  row = treePosition[0]
  col = treePosition[1]
  height = trees[row][col]
  treesRow = trees[treePosition[0]]
  treesCol = [i[col] for i in trees]

  ## top
  for tree in treesCol[row-1::-1]:
    top += 1
    if tree < height:
      continue
    else:
      break

  ## left
  for tree in treesRow[col-1::-1]:
    left += 1
    if tree < height:
      continue
    else:
      break

  ## right
  for tree in treesRow[col+1:]:
    right += 1
    if tree < height:
      continue
    else:
      break
  
  ## bottom
  for tree in treesCol[row+1:]:
    bottom += 1
    if tree < height:
      continue
    else:
      break

  return left * right * top * bottom

highestScore = 0
for row in range(0, len(trees)):
  for col in range(len(trees[0])):
    highestScore = max(highestScore, findScore((row, col)))
print(highestScore)