import json

file_name = 'number.json'

with open(file_name, 'r') as fobj:
    numbers = json.load(fobj)

print(numbers)
