f = open('input.txt', 'r')
lines = f.readlines()
### cid is optional
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passports = []
for line in lines:
  if line.startswith('\n'):
    if len(required_fields) > 0:
      passports.append(False)
    else:
      passports.append(True)
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  else:
    fields = dict((key.strip(), value.strip()) 
                   for key, value in (field.split(':')
                   for field in line.split(' ')))
    for actual_field in fields.keys():
      if actual_field in required_fields:
        required_fields.remove(actual_field) 
  
print(passports.count(True))
