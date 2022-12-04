# https://adventofcode.com/2022/day/1

file = open("input.txt", "r")
totalCalories = file.read()
runningCount = 0
maxCalories = 0
for cal in totalCalories.split('\n'):
  if not cal:
    maxCalories = max(maxCalories, runningCount)
    runningCount = 0
  else:
    runningCount += int(cal)
print(maxCalories)