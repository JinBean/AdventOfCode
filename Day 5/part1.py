# https://adventofcode.com/2022/day/5

file1 = open("crates_transposed.txt", "r")
results = file1.read()
crates = results.strip().split('\n')

file2 = open("instructions.txt", "r")
results = file2.read()
instructions = results.strip().split('\n')
simplified_instructions = list(map(lambda x: [int(i) for i in x.split(' ') if i.isnumeric()], instructions))

for inst in simplified_instructions:
  fromCrate = crates[inst[1]-1]
  toCrate = crates[inst[2]-1]
  crates[inst[1]-1] = fromCrate[:len(fromCrate)-inst[0]]
  crates[inst[2]-1] = toCrate + fromCrate[len(fromCrate)-inst[0]:][::-1]

print(''.join([crate[-1:] for crate in crates]))