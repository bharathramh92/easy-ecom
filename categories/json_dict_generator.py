import json

with open('categories.json') as data_file:
    data = "category_dict = "+ str(json.load(data_file))
file = open('category_from_json.py', 'w')
file.write(data)
file.close()