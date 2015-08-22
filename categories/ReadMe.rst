Upon updation of category model, the following commands has to be run.
All commands are from project root directory
generate the category dump:
    ./manage.py dumpdata categories.Category --indent 2 --format json >categories/categories.json
genarate dictionary from above generated json:
    python categories/category_dict_json_output.py