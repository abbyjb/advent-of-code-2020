import sys
### Read Input
f = open('input.txt', 'r')
lines = f.readlines()
### store line length for modular arithmetic
line_length = len(lines[0]) - 1


trees = 0
current_position_right = 0
current_position_down = 0
right = int(sys.argv[1])
down = int(sys.argv[2])
for line in lines:
  ### depending on down value, skip
  if current_position_down % down  == 0:
    ### account for the involving arboreal genetics and biome stability :p
    current_position_right = current_position_right % line_length
    if line[current_position_right] == '#':
      trees += 1
    current_position_right += right
  current_position_down += 1

print('right:', right, 'down:', down, 'trees:', trees)
