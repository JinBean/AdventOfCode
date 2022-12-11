# https://adventofcode.com/2022/day/11
import math

with open("input.txt", "r") as file:
  input = file.read()
  monkeys = input.strip().split('\n\n')

op = {
  '+': lambda x, y: x + y,
  '-': lambda x, y: x - y,
  '*': lambda x, y: x * y,
  }

monkeyInfo = []
for enum, i in enumerate(monkeys):
  info = i.split('\n')
  startingItems = (info[1].split('items: '))[1].split(', ')
  monkeyInfo.append({
    'items': [int(x) for x in startingItems],
    'operation': info[2].split(' ')[-2],
    'opValue': info[2].split(' ')[-1],
    'test': int(info[3].split('by ')[1]),
    'true': int(info[4].split(' ')[-1]),
    'false': int(info[5].split(' ')[-1]),
    'active': 0
    })
  
for i in range(20):
  for monkey in monkeyInfo:
    items = monkey['items'].copy()
    monkey['active'] += len(items)
    for item in items:
      opValue = item if monkey['opValue'] == 'old' else int(monkey['opValue'])
      newItem = math.floor(op[monkey['operation']](item, opValue) / 3)
      if newItem%monkey['test'] == 0:
        monkeyInfo[monkey['true']]['items'].append(newItem)
      else:
        monkeyInfo[monkey['false']]['items'].append(newItem)
      monkey['items'].pop(0)

active = [m['active'] if m['active'] else 0 for m in monkeyInfo]
active.sort(reverse=True)
print(active[0] * active[1])