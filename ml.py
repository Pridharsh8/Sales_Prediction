from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import numpy as np
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to the appropriate origins in production
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)
class model_input(BaseModel):
    Item_Identifier: int
    Item_Weight: float
    Item_Fat_Content: int
    Item_Visibility: float
    Item_Type: int
    Item_MRP: float
    Outlet_Identifier: int
    Outlet_Establishment_Year: int
    Outlet_Size: int
    Outlet_Location_Type: int
    Outlet_Type: int

sales_model = pickle.load(open('Foml.pickle', 'rb'))


@app.post('/bigmart_prediction')
def sal_predict(input_parameters: model_input):
    input_data = input_parameters.dict()
    
    Ident = input_data['Item_Identifier']
    Weigh = input_data['Item_Weight']
    Fat = input_data['Item_Fat_Content']
    Vsi = input_data['Item_Visibility']
    Type = input_data['Item_Type']
    MRP = input_data['Item_MRP']
    o_Ident = input_data['Outlet_Identifier']
    Year = input_data['Outlet_Establishment_Year']
    Size = input_data['Outlet_Size']
    Loc = input_data['Outlet_Location_Type']
    o_type = input_data['Outlet_Type']

    input_list = [Ident, Weigh, Fat, Vsi, Type, MRP, o_Ident, Year, Size, Loc, o_type]
    
    prediction = sales_model.predict([input_list])[0]  # Extract the first element from the prediction array
    
    return {"prediction": prediction.item()}  # Convert prediction to a native Python data type and return as a JSON response
