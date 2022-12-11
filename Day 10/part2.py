# https://adventofcode.com/2022/day/10


with open("input.txt", "r") as file:
  input = file.read()
  signals = input.strip().split('\n')

strength = [1]
total = 1
for signal in signals:
  if signal == 'noop':
    strength.append(total)
  else:
    strength.append(total)
    total += int(signal.split(' ')[1])
    strength.append(total)


crt = []
for i in range(len(strength)):
  currentValue = strength[i]
  signalRange = [currentValue-1, currentValue, currentValue+1]
  if i%40 in signalRange:
    crt.append('#')
  else:
    crt.append('.')

for i in range(0, len(crt)-1, 40):
  print(''.join(crt[i:i+40]))