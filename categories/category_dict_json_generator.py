import json

with open('categories.json') as data_file:
    data = "category_dict = "+ str(json.load(data_file))
file = open('category_dict_json_output.py', 'w')
file.write(data)
file.close()