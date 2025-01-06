import json
#JSON is a builtin package that is used to work with python data and it converts python data into json data.
# function
# 1. dumps(data): it is used to convert python data into json data
data = {'name': 'ali',
        'roll_no': 101
        }
json_data = json.dumps(data)
print(json_data)

# 2. loads(): it convert json data into python data
python_data = json.dumps(json_data)
print(python_data)