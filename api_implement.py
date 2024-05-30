# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 21:08:24 2024

@author: pridh
"""

import json
import requests



url='http://127.0.0.1:8000/bigmart_prediction'
input_data_for_model={
    'Item_Identifier':30,
    'Item_Weight':201.5,
    'Item_Fat_Content':6,
    'Item_Visibility':21.7,
    'Item_Type':8,
    'Item_MRP':90.0,
    'Outlet_Identifier':10,
    'Outlet_Establishment_Year':2000,
    'Outlet_Size':104,
    'Outlet_Location_Type':65,
    'Outlet_Type':2
    
    
    }
input_json=json.dumps(input_data_for_model)
response=requests.post(url, data=input_json)
print(response.status_code)

print(response.text)