# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:51:38 2024

@author: pridh
"""

import json
import requests

url = 'http://127.0.0.1:8000/bigmart_prediction'
input_data_for_model = {
    'Item_Identifier': 156,
    'Item_Weight': 9.30,
    'Item_Fat_Content': 0,
    'Item_Visibility': 0.016047,
    'Item_Type': 4,
    'Item_MRP': 249.8092,
    'Outlet_Identifier': 9,
    'Outlet_Establishment_Year': 1999,
    'Outlet_Size': 1,
    'Outlet_Location_Type': 0,
    'Outlet_Type': 1
}

input_json = json.dumps(input_data_for_model)
response = requests.post(url, json=input_data_for_model)

print("Status code:", response.status_code)
print("Response text:", response.text)
