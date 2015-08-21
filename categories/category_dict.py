import json

category = {
    'parent_id': None,
    "Books":
        {
            'parent_id': 1,
            'Engineering & Transportation':
                 {
                     'parent_id': 2,
                     'Engineering':
                      {
                          'parent_id': 3,
                          'Electrical & Electronics':
                           {
                               'parent_id': 4,
                               'Electronics' :
                                   {
                                       'parent_id': 5,
                                       'Opto Electronics' : {'id':6},
                                       'Transistors' : {'id':7},
                                       'Solid State' : {'id':8},
                                       'Semiconductors': {'id':9}
                                   },
                           },
                      },
                  },
            'Science & Math':
                {
                    'parent_id': 1,
                    'Mathematics':{
                        'parent_id': 11,
                        'Infinity':{'id':12},
                        'Matrics':{'id':13},
                        'Trigonometry' :{'id':14},
                    },
                    'Physics':{'id':15},
                },
             },
}

def get_category_list_data_json():
    return json.dumps(category)

def get_category_list_dict():
    return category

def get_end_categories(path):
    """
    path should be like "Books > Engineering & Transportation >  Engineering". ie space to left and right of > symbol.
    :param path:
    :return: returns dict with key names as category names and id as their value
    """
    categories = {}
    path = path.split(' > ')
    category_data = category
    while True:
        try:
            #Getting in to the given path in dict.
            category_data = category_data[path.pop(0)]
        except Exception:
            break
    def go_below(category_data):
        for k, v in category_data.items():
            if k not in ['id', 'parent_id']:
                try:
                    categories[k] = v['id']
                except Exception:
                    go_below(category_data[k])
    go_below(category_data)
    return categories

def get_next_sub_category(path):
    """
    path should be like "Books > Engineering & Transportation >  Engineering". ie space to left and right of > symbol.
    :param path:
    :return: returns dict. Key name 'list' has dict with key as category name and id as their value. Key end_level is boolean, true if end level reached.
    """
    categories = {}
    path = path.split(' > ')
    category_data = category            #since we are navigating into the category by pop() method.
    while True:
        try:
            #Getting in to the given path in dict.
            category_data = category_data[path.pop(0)]
        except Exception:
            break
    end_level = False
    for k, v in category_data.items():
        if k not in ['id', 'parent_id']:
            try:
                categories[k] = v['id']
                end_level = True
            except Exception:
                categories[k] = v['parent_id']
    return {'categories': categories, 'end_level': end_level}