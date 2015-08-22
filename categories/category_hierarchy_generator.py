import json
from collections import defaultdict
from category_dict_json_output import category_dict

def get_category_raw_dict():
    """
    :output: sample: {1: {'parent_category': None, 'category_name': 'Books', 'description': ''}, 2: {'parent_category': 1, 'category_name': 'Engineering & Transportation', 'description': ''}, 3: {'parent_category': 2, 'category_name': 'Engineering', 'description': ''}, 4: {'parent_category': 3, 'category_name': 'Electrical & Electronics', 'description': ''}, 5: {'parent_category': 4, 'category_name': 'Electronics', 'description': ''}, 6: {'parent_category': 5, 'category_name': 'Opto Electronics', 'description': ''}, 7: {'parent_category': 5, 'category_name': 'Transistors', 'description': ''}, 8: {'parent_category': 5, 'category_name': 'Solid State', 'description': ''}, 9: {'parent_category': 5, 'category_name': 'Semiconductors', 'description': ''}, 10: {'parent_category': 1, 'category_name': 'Science & Math', 'description': ''}, 11: {'parent_category': 10, 'category_name': 'Mathematics', 'description': ''}, 12: {'parent_category': 11, 'category_name': 'Infinity', 'description': ''}, 13: {'parent_category': 11, 'category_name': 'Matrics', 'description': ''}, 14: {'parent_category': 11, 'category_name': 'Trigonometry', 'description': ''}, 15: {'parent_category': 10, 'category_name': 'Physics', 'description': ''}}
    :return:
    """
    category_data_dict= {}
    for items in category_dict:
        category_data_dict[items['pk']] = items['fields']
    return category_data_dict

def get_category_hierarchy():
    """
    output sample:{1: {2: {3: {4: {5: {8: {}, 9: {}, 6: {}, 7: {}}}}}, 10: {11: {12: {}, 13: {}, 14: {}}, 15: {}}}}
    :return:
    """
    list_data = defaultdict(list)
    for items in category_dict:
        list_data[items['fields']['parent_category']].append((items['pk'], items['fields']['category_name'], items['fields']['parent_category']))
    def build_tree(dict, index):
        return {pk: build_tree(dict, pk) for pk, name, parent_id in dict[index]}
    return build_tree(list_data, None)