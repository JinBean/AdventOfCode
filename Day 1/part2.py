file = open("input.txt", "r")
totalCalories = file.read()

def parseCalorieString(calorieString):
  calories = calorieString.strip().split('\n')
  total = sum(map(int, calories))
  return total

splitCalories = totalCalories.split('\n\n')
calorieList = map(parseCalorieString, splitCalories)
top3 = sorted(calorieList)[-3:]
print(sum(top3))

