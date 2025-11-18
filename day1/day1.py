### Read files
f = open('input.txt', 'r')
lines = f.readlines()
total = 2020
report = []
for line in lines:
  report.append(int(line.strip('\n')))



### Part 1
current_index = 0
target = 2020
found = False
while not found:
  for i in range(0, len(report)):
    if i != current_index:
      if report[current_index] + report[i] == target:
        print(report[current_index], report[i])
        found = True
  current_index += 1



### Part 2
found = False
while not found:
  for i in range(0, len(report)):
    for j in range(i + 1, len(report)):
      if i != current_index:
        if report[current_index] + report[i] + report[j] == target:
          print(report[current_index], report[i], report[j])
          found = True
  current_index += 1      
