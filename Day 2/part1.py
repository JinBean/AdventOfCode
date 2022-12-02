'''
The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.
'''

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
