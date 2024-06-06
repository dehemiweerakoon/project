import json
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

__model = None

def get_result(gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level):
    load_saved_artifacts()
    x = np.zeros(8)
    x[0] = 0 if gender == 'female' else 1
    x[1] = age
    x[2] = hypertension
    x[3] = heart_disease
    x[4] = smoking_history  # This should be a numerical value as provided by frontend
    x[5] = bmi
    x[6] = HbA1c_level
    x[7] = blood_glucose_level
    return __model.predict([x])[0]

def load_saved_artifacts():
    global __model
    with open("./art/model.pickle", 'rb') as f:
        __model = pickle.load(f)  # Use pickle.load to load from file
    print("Loading saved artifacts... done")

if __name__ == "__main__":
    load_saved_artifacts()