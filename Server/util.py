import pickle
import json
import numpy as np

__city = None
__data_columns = None
__model = None
def get_estimated_price(city,bedroom, bathroom, sqft_living, sqft_lot,floors, view, condition, sqft_basement):
    try:
        locate_index= __data_columns.index(city.lower())
    except:
        locate_index= -1
    x=np.zeros(len(__data_columns))
    x[0] = bedroom
    x[1] = bathroom
    x[2] = sqft_living
    x[3] = sqft_lot
    x[4] = floors
    x[5] = view
    x[6] = condition
    x[7] = sqft_basement

    if locate_index >=0:
        x[locate_index] = 1
    return round(__model.predict([x])[0],2 )

def get_city():
    return __city

def load_saved_artificats():
    print("loading saved artifacts.....")
    global __city
    global __data_columns
    with open("./artifects/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __city = __data_columns[8:]
    global __model
    with open("./artifects/Home_prices_model.pickle",'rb') as f:
        __model= pickle.load(f)
    print("loading saved artifacts done")

if __name__ == "__main__":
    load_saved_artificats()
    print(get_city())
    print(get_estimated_price('kent',3,2,1930,11947,1,0,4,0))

