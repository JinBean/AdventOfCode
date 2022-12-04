# https://adventofcode.com/2022/day/2

# A = Rock = X
# B = Paper = Y
# C = Scissors = Z

selection = ['X', 'Y', 'Z']
outcome = {
  'X': ['B', 'A', 'C'],
  'Y': ['C', 'B', 'A'],
  'Z': ['A', 'C', 'B'],
}

file = open("input.txt", "r")
results = file.read()
rounds = results.strip().split('\n')

def calcRoundScore(round):
  options = round.split(' ')
  selectionScore = selection.index(options[1]) + 1
  score = (outcome[options[1]].index(options[0]) * 3)
  return score + selectionScore

print(sum(map(calcRoundScore, rounds)))
