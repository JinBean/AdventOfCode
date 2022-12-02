'''
"Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated.
'''


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

