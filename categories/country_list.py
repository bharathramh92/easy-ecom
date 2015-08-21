import json
country = {"India" :
            {
                "Kerala":
                       ["Trivandrum", "Kochi","Munnar","Kozhikode","Kollam","Alappuzha","Thrissur",
                        "Kottayam","Palakkad","Kannur","Emakulam","Wayanad"],
                "Tamil Nadu":
                   ["Chennai", "Madurai","Coimbatore","Salem","Erode","Vellore"],
                "Andaman & Nicobar Islands":
                    ["Bamboo Flat","Garacharma","Port Blair","Prothrapur"],
                "Andhra Pradesh":
                    ["Vijayawada","Visakapatnam","Guntur","Nellore","Kurnool","Tirupathi"],
                "Arunachal Pradesh":
                    ["Aalo","Itanagar","Naharlagun","Pasighat"],
                "Assam":
                    ["Guwahati","Silchar","Jorhat","Nagaon","Tezpur","Diphu"],
                "Delhi":
                    ["Delhi","Jaffarpur Kalan","Qutabgarh","Ujwa"],
                "Goa":
                    ["Panaji","Madgaon","Mormugao"],
                "Gujarat":
                    ["Ahmadabad","Surat","Vadodara","Rajkot"],
                "Harayana":
                    ["Faridabad","Gurgaon","Panipat","Hisar"],
                "Himachal Pradesh":
                    ["Baddi","Chamba","Dharmsala","Kullu","Mandi","Shimla"],
                "Karnataka":
                    ["Bengaluru","Mysore","Mangalore","Belgaum","Bellary"],
                "Madhya Pradesh":
                    ["Indore","Bhopal","Gwalior","Sagar"],
                "Maharashtra":
                    ["Mumbai","Pune","Nagpur","Nashik"],
                "Punjab":
                    ["Ludhiana","Amritsar","Jalandhar","Patiala"],
                "Rajasthan":
                    ["Jaipur","Jodhpur","Kota","Ajmer"],
                "Telangana":
                    ["Hyderabad","Warangal","Nizamabad","Karimnagar","Nalgonda"],
                "West Bengal":
                    ["Kolkata","Asansol","Habra","Kharagpur"]
            },
            "United States" :

            {
                "North Carolina":
                       ["Charlotte", "Raleigh"],
                "California":
                       ["Silicon Valley", "Los Angeles"],

                "Virginia" :
                       ["Richmond" , "Fairfax"],
                "District of Colombia" :
                       ["Washington DC"],
                "South Carolina":
                       ["Columbia","Charleston"],
                "Georgia":
                       ["Atlanta","Columbus"],
                "Florida":
                       ["Miami","Jacksonville"],
                "Maryland":
                       ["Baltimore","Annapolis"],
                "Texas":
                       ["Austin","Dallas"],
                "Minnesota":
                       ["Saint paul","Minneapolis"],
                "Neavada":
                       ["Las vegas","Carson city"],
                "New Jersey":
                       ["Trenton","Newark"],
                "NewYork":
                       ["Newyorkcity","Albany"],
                "Ohio":
                       ["Columbus","Cincinatti"]
            }
        }

def get_country_list_data_json():
    return json.dumps(country)

def get_country_list_dict():
    return country

def get_country_names():
    country_name = []
    for country_data in country.keys():
        country_name.append(country_data)
    return country_name

def get_state_names(country_name):
    try:
        state_names = []
        for state_name in country[country_name].keys():
            state_names.append(state_name)
        return state_names
    except KeyError:
        return None

def get_city_names(country_name, state):
    try:
        return country[country_name][state]
    except KeyError:
        return None