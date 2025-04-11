import pickle
import json
import numpy as np

_data_columns = None
_model = None


def get_calorie(gender,age,height,weight,duration,heart_rate,body_temp):

    x = np.zeros(len(_data_columns))
    x[0] = gender
    x[1] = age
    x[2] = height
    x[3] = weight
    x[4] = duration
    x[5]=heart_rate
    x[6]=body_temp

    return round(_model.predict([x])[0], 2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  _data_columns

    with open("./artifacts/columns.json", "r") as f:
        _data_columns = json.load(f)['data_columns']

    global _model
    if _model is None:
        with open('artifacts/pridict_model.pickle', 'rb') as f:
            _model = pickle.load(f)
    print("loading saved artifacts...done")


def get_data_columns():
    return _data_columns

if __name__ == '__main__':
    load_saved_artifacts()
