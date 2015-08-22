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
                                       'Opto Electronics' :
                                           {
                                               'parent_id':6,
                                           },
                                       'Transistors' :
                                           {
                                               'parent_id':7,
                                           },
                                       'Solid State' :
                                           {
                                               'parent_id':8,
                                           },
                                       'Semiconductors':
                                           {
                                               'parent_id':9,
                                           }
                                   },
                           },
                      },
                  },
            'Science & Math':
                {
                    'parent_id': 1,
                    'Mathematics':
                        {
                            'parent_id': 11,
                            'Infinity':{
                                'parent_id':12,
                            },
                            'Matrics':
                                {
                                    'parent_id':13,
                                },
                            'Trigonometry' :
                                {
                                'parent_id':14,
                                },
                        },
                    'Physics':
                        {
                            'parent_id':15,
                        },
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
            if k not in ['parent_id']:
                if len(v)==1:
                    categories[k] = v['parent_id']
                else:
                    go_below(category_data[k])
    go_below(category_data)
    return categories

def get_next_sub_category(path):
    """
    path should be like "Books > Engineering & Transportation >  Engineering". ie space to left and right of > symbol.
    :param path:
    :return: returns dict. Key name 'categories' has dict with key as category names and values is list of a dict,
    whose 'id' refers to category id and 'end_level' refers to the condition whether it is the last level.
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
    for k, v in category_data.items():
        if k not in ['parent_id']:
            categories[k] = [{'id': v['parent_id'], 'end_level':'True' if len(v)==1 else 'False'}]
    return {'categories': categories}


if __name__ == '__main__':
    path = 'Books > Science & Math'
    print(get_end_categories(path))
    # print(get_next_sub_category(path))