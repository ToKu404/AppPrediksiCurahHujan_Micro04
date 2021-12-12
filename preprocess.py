import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocessing(data):
    data = [np.array(data)]
    data = pd.DataFrame(data)
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    return data