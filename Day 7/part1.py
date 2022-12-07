# https://adventofcode.com/2022/day/7

file = open("input.txt", "r")
input = file.read()
instructions = input.strip().split('\n')

dirSize = {}

for inst in instructions:
  if inst.startswith('$ cd'):
    dirName = inst.split('$ cd ')[1]
    if dirName == '/':
      dirPath = ['/']
    elif dirName == '..':
      dirPath.pop()
    else: # cd into new dir
      dirPath.append(dirName)

  elif inst.startswith('$ ls'):
    continue

  else: # not cd command
    if inst.startswith('dir'):
      continue
    else: # file size
      fileSize = int(inst.split(' ')[0])
      for i in range(len(dirPath)):
        joinedPath = '/'.join(dirPath[:i+1])
        if joinedPath in dirSize:
          dirSize[joinedPath] += fileSize
        else:
          dirSize[joinedPath] = fileSize


total = 0
for key, value in dirSize.items():
  if value <= 100000:
    total += value
print(total)