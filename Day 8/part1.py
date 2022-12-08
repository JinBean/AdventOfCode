# https://adventofcode.com/2022/day/8

file = open("input.txt", "r")
input = file.read()
trees = input.strip().split('\n')

def rotate90(matrix, times=1):
  for i in range(times):
    matrix = list(zip(*matrix[::-1]))
  return matrix

trees = [[x for x in i] for i in trees]
trees90 = rotate90(trees)
trees180 = rotate90(trees90)
trees270 = rotate90(trees180)

height = (len(trees))
width = len(trees[0])

def getVisible(trees):
  mappedVisible = [[0 for x in i] for i in trees]
  highestTrees = [int(i) for i in trees[0]]
  for row in range(0, len(trees)):
    for treeIndex in range(len(trees[0])):
      if (int(trees[row][treeIndex]) > int(highestTrees[treeIndex])):
        mappedVisible[row][treeIndex] = 1
        highestTrees[treeIndex] = trees[row][treeIndex]
  return mappedVisible

visible = getVisible(trees)
visible90 = getVisible(trees90)
visible180 = getVisible(trees180)
visible270 = getVisible(trees270)

mappedTop = visible
mappedLeft = rotate90(visible90, 3)
mappedBottom = rotate90(visible180, 2)
mappedRight = rotate90(visible270, 1)

total = (height * 2) + (width * 2) - 4
for row in range(1, len(trees)-1):
  for col in range(1, len(trees[0])-1):
    vis = mappedTop[row][col] or mappedLeft[row][col] or mappedBottom[row][col] or mappedRight[row][col]
    if vis:
      total += 1

print(total)
