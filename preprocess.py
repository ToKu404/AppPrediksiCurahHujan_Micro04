import numpy as np
import pickle

def preprocessing(data):
    data = [np.array(data)]
    scaler = pickle.load(open("scaler.pkl","rb"))
    data = scaler.transform(data)
    return data