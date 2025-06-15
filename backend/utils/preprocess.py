import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

le_sex = joblib.load('models/le_sex.pkl')
le_smoker = joblib.load('models/le_smoker.pkl')
le_region = joblib.load('models/le_region.pkl')
scaler = joblib.load('models/scaler.pkl')

def preprocess_input(data):
    df = pd.DataFrame([data], columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])
    df['sex'] = le_sex.transform([df['sex'].iloc[0]])[0]
    df['smoker'] = le_smoker.transform([df['smoker'].iloc[0]])[0]
    df['region'] = le_region.transform([df['region'].iloc[0]])[0]
    numeric_cols = ['age', 'bmi', 'children']
    df[numeric_cols] = scaler.transform(df[numeric_cols])
    return df