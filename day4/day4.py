import re

def validate_passport(fields):
  valid = True
  for key, value in fields.items():
    print(key, value)
    if key == 'byr':
      value = int(value)
      valid = valid and (value >= 1920 and value <= 2002)
      required_fields.remove('byr')
    elif key == 'iyr':
      value = int(value)
      valid = valid and (value >= 2010 and value <= 2020)
      required_fields.remove('iyr')
    elif key == 'eyr':
      value = int(value)
      valid = valid and (value >= 2020 and value <= 2030)
      required_fields.remove('eyr')
    elif key == 'hgt':
      if value.endswith('cm') or value.endswith('in'):
        height = int(value[:-2])
        if value.endswith('cm'):
          valid = valid and (height >= 150 and height <= 193)
        else:
          valid = valid and (height >= 59 and height <= 76)
      else:
        return False
      required_fields.remove('hgt')
    elif key == 'hcl':
      hex_color_regex = '#[0-9a-f]{6}'
      match = re.findall(hex_color_regex, value)
      if len(match) == 0:
        return False      
      required_fields.remove('hcl')
    elif key == 'ecl':
      valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
      if value not in valid_ecl:
        return False
      required_fields.remove('ecl')
    elif key == 'pid':
      pid_regex = '\d{9}'
      match = re.findall(pid_regex, value)
      if len(match) == 0:
        return False
      required_fields.remove('pid')
    print(valid)
  return valid

f = open('input.txt', 'r')
lines = f.readlines()
### cid is optional
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passports = []
validated = True
for line in lines:
  if line.startswith('\n'):
    if validated and len(required_fields) == 0:
      passports.append(True)
    else:
      passports.append(False)
      validated = True
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  else:
    fields = dict((key.strip(), value.strip()) 
                   for key, value in (field.split(':')
                   for field in line.split(' ')))
    validated = validated and validate_passport(fields)

print(passports, passports.count(True))
