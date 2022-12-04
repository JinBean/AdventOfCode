# A = Rock = X
# B = Paper = Y
# C = Scissors = Z

selection = ['X', 'Y', 'Z']
outcome = {
  'A': ['Z', 'X', 'Y'],
  'B': ['X', 'Y', 'Z'],
  'C': ['Y', 'Z', 'X']
}

file = open("input.txt", "r")
results = file.read()
rounds = results.strip().split('\n')

def calcRoundScore(round):
  options = round.strip().split(' ')
  select = outcome[options[0]][selection.index(options[1])]
  score = selection.index(select) + 1
  selectionScore = (selection.index(options[1]) * 3)
  return score + selectionScore

print(sum(map(calcRoundScore, rounds)))

