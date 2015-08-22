Upon updating the category model, the following commands has to be run.
generate the category dump:(from project root folder)
    ./manage.py dumpdata categories.Category --indent 2 --format json >categories/categories.json
generate dictionary from above generated json:(from categories app folder)
    python category_dict_json_output.py