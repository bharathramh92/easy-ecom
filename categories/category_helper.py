import json
from categories.category_hierarchy_generator import get_category_raw_dict, get_category_hierarchy

def get_category_list_data_json():
    return json.dumps(get_category_raw_dict())

def get_category_list_dict():
    return get_category_raw_dict()

def sanitize(path):
    if path == '':
        return []
    return path.replace(" > ", ">").split('>')

def get_name_id_dict():
    name_id_dict = {}
    for k,v in get_category_raw_dict():
        name_id_dict[v['category_name']] = k
    return name_id_dict

def go_into_path(category_data, path):
    while True:
        try:
            #Getting in to the given path in dict.
            category_data = category_data[int(path.pop(0))]
        except IndexError:
            break
        except (KeyError, ValueError):
            raise ValueError("Invalid path")
    return category_data

def get_end_categories(path):
    """
    path should be like "1 > 2 > 3". ie space to left and right of > symbol.
    :param path:
    :return: returns dict with key names as category names and id as their value
    """
    category_raw = get_category_raw_dict()
    categories = {}
    path = sanitize(path)
    category_data = get_category_hierarchy()
    go_into_path(category_data, path)
    def go_below(category_data):
        for k, v in category_data.items():
            if bool(v):
                go_below(category_data[k])
            else:
                categories[category_raw[k]['category_name']] = k
    go_below(category_data)
    return categories

def get_next_sub_category(path):
    """
    path should be like "1 > 2 > 3". ie space to left and right of > symbol.
    :param path:
    :return: returns dict. Key name 'categories' has dict with key as category id and values is a boolean
    which refers to the condition whether it is the last level or not.
    """
    categories = {}
    path = sanitize(path)
    category_data = get_category_hierarchy()            #since we are navigating into the category by pop() method.
    go_into_path(category_data, path)
    for k, v in category_data.items():
        categories[k] = 'False' if bool(v) else 'True'
    return {'categories': categories}

def get_reverse_path(pk):
    """
    :param pk:
    :return:list of dict in reverse order where keys are category name values are category id
    """
    category_raw = get_category_raw_dict()
    path=[]
    def go_up(pk):
        path.append({category_raw[pk]['category_name']:pk})
        try:
            return go_up(category_raw[pk]['parent_category'])
        except Exception:
            pass
    go_up(pk)
    return path[::-1]

def get_category_name(pk):
    return get_category_raw_dict()[pk]['category_name']

def get_category_store_names():
    """
    :return:Return first level names of category, which is defined as store
    """
    return {'store_names': {get_category_name(k): k} for k in get_next_sub_category('')['categories'].keys()}

def get_store_end_categories(store_name):
    return get_end_categories(str(get_category_store_names()['store_names'][store_name]))

# if __name__ == '__main__':
#     path = '1'
#     print('reverse path is ',get_reverse_path(9))
#     print('end category is ', get_end_categories(path))
#     print('next sub category is ', get_next_sub_category(path))
#     print('category name is ', get_category_name(5))
#     print('store names are ', get_category_store_names())
#     print('get_store_end_categories', get_store_end_categories('Books'))