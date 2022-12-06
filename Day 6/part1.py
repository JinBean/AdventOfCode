# https://adventofcode.com/2022/day/6

file = open("input.txt", "r")
stream = file.read()

def findMarker(markerLength):
  buffer = stream[:markerLength]
  for enum, i in enumerate(stream[markerLength-1:]):
    buffer = buffer[1:] + i
    if len(buffer) == len(set(buffer)):
      break
  return enum + markerLength


print(findMarker(4))
  