# https://adventofcode.com/2022/day/13
import json

with open("input.txt", "r") as file:
  input = file.read()
  values = input.strip().split('\n\n')

def compareOuterInputs(left, right):
  if left == right:
    return None
  for i in range(len(left)):
    try:
      comparison = compareInputs(left[i], right[i])
      match (comparison):
        case 1:
          return True
        case 2:
          continue
        case 3:
          return False
    except IndexError:
      return False
  return True

def compareInputs(left, right):
  if isinstance(left, list) and isinstance(right, list):
    result = compareOuterInputs(left, right)
  elif isinstance(left, list) and not isinstance(right, list):
    result = compareOuterInputs(left, [right])
  elif not isinstance(left, list) and isinstance(right, list):
    result = compareOuterInputs([left], right)
  elif left < right:
    return 1 # pass
  elif left == right:
    return 2 # continue
  elif left > right:
    return 3 # fail
  else:
    print('inputs fell through: {} and {}'.format(left, right))
  match (result):
    case True:
      return 1
    case False:
      return 3
    case None:
      return 2


results = []
def findOrder():
  for enum, value in enumerate(values):
    x, y = value.split('\n')
    first = json.loads(x)
    second = json.loads(y)
    result = compareOuterInputs(first, second)
    if result:
      results.append(enum+1)

findOrder()
print(sum(results))