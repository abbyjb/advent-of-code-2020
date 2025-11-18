### Read input
f = open('input.txt', 'r')
lines = f.readlines()
num_valid = 0
for line in lines:
  ## parse line of password to extract the lower bound, upper bound, the letter
  ## to check, and the password itself
  corporate_rule, password = line.strip('\n').split(': ')
  constraints, letter = corporate_rule.split(' ')
  lower_bound, upper_bound = map(lambda x: int(x), constraints.split('-'))
  
  ### part 1: constraints as bounds of occurences 
  num_occurences = password.count(letter)
  if num_occurences in range(lower_bound, upper_bound + 1):
    num_valid += 1
  

print("part 1:", num_valid)

num_valid = 0
for line in lines:
  ## parse line of password to extract the lower bound, upper bound, the letter
  ## to check, and the password itself
  corporate_rule, password = line.strip('\n').split(': ')
  constraints, letter = corporate_rule.split(' ')
  # shift positions down 1 because elves don't account for index 0
  first_position, second_position = map(lambda x: int(x) - 1, constraints.split('-'))

  ### part 2: constraints as positions in password
  first_letter, second_letter = [password[first_position], password[second_position]]
  if (first_letter == letter) ^ (second_letter == letter):
    num_valid += 1   

print("part 2:", num_valid)
