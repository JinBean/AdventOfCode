# https://adventofcode.com/2022/day/10


with open("input.txt", "r") as file:
  input = file.read()
  signals = input.strip().split('\n')

strength = [0]
for signal in signals:
  if signal == 'noop':
    strength.append(0)
  else:
    strength.append(0)
    strength.append(int(signal.split(' ')[1]))

totalSignalStrength = 0
for i in range(20, 260, 40):
  signalStrength = (sum(strength[:i])+1) * i
  totalSignalStrength += signalStrength
print(totalSignalStrength, '\n')
