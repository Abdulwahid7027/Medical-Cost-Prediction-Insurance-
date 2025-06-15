import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
import joblib
import os

df = pd.read_csv('data/insurance.csv')
le_sex = LabelEncoder()
le_smoker = LabelEncoder()
le_region = LabelEncoder()

df['sex'] = le_sex.fit_transform(df['sex'])
df['smoker'] = le_smoker.fit_transform(df['smoker'])
df['region'] = le_region.fit_transform(df['region'])
df['charges'] = np.log1p(df['charges'])

scaler = StandardScaler()
numeric_cols = ['age', 'bmi', 'children']
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

X = df.drop('charges', axis=1)
y = df['charges']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

xgb = XGBRegressor(n_estimators=200, max_depth=5, learning_rate=0.05, random_state=42)
lgbm = LGBMRegressor(n_estimators=200, max_depth=5, learning_rate=0.05, random_state=42)
catboost = CatBoostRegressor(n_estimators=200, max_depth=5, learning_rate=0.05, random_state=42, verbose=0)

xgb.fit(X_train, y_train)
lgbm.fit(X_train, y_train)
catboost.fit(X_train, y_train)

os.makedirs('models', exist_ok=True)
joblib.dump(xgb, 'models/xgb_model.pkl')
joblib.dump(lgbm, 'models/lgbm_model.pkl')
joblib.dump(catboost, 'models/catboost_model.pkl')
joblib.dump(le_sex, 'models/le_sex.pkl')
joblib.dump(le_smoker, 'models/le_smoker.pkl')
joblib.dump(le_region, 'models/le_region.pkl')
joblib.dump(scaler, 'models/scaler.pkl')

print("Models and preprocessors saved successfully.")