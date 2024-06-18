import json

with open('../get_pwd.py', 'r') as f:
    data = json.load(f)

print(data['PWD'])
