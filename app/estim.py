import pickle
import numpy as np
def estim1(vals):
    val1 = float(vals[0])
    val2 = float(vals[1])
    val3 = float(vals[2])
    linmodel = pickle.load(open("app/finalized_model.sav", 'rb'))
    x1 = np.array([[val1, val2, val3]])
    return float(linmodel.predict(x1))