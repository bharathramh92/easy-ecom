import json

category = {
    "Books":
        {
            'Engineering & Transportation':
                 {
                     'Engineering':
                      {
                          'Electrical & Electronics':
                           {
                               'Electronic' :
                                   {
                                       'Opto Electronics' : {}, 'Transistors' : {}, 'Solid State' : {}, 'Semiconductors': {}
                                   },
                           },
                      },
                  },
            'Science & Math':
                {
                    'Mathematics':{
                        'Infinity':{},'Matrics':{}, 'Trigonometry' :{},
                    },
                    'Physics':{},
                },
             },
}

def get_category_list_data_json():
    return json.dumps(category)

def get_category_list_dict():
    return category

def get_bottom_category_names(path):
    list = []
    path = path.split(' > ')
    category_data = category
    while True:
        try:
            category_data = category_data[path.pop(0)]
        except Exception:
            break
    def go_below(category_data):
        for k, v in category_data.items():
            if bool(v):
                go_below(category_data[k])
            else:
                list.append(k)
    go_below(category_data)
    return list