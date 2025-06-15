import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor
from sklearn.metrics import r2_score, mean_squared_error

# Load dataset
data = pd.read_csv('../data/insurance.csv')

# Preprocessing
data = pd.get_dummies(data, drop_first=True)
X = data.drop('charges', axis=1)
y = data['charges']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
xgb_model = XGBRegressor(n_estimators=100, learning_rate=0.1)
cat_model = CatBoostRegressor(iterations=100, learning_rate=0.1, verbose=0)  # Set verbose=0 to suppress output
lgbm_model = LGBMRegressor(n_estimators=100, learning_rate=0.1)

# Fit models
xgb_model.fit(X_train, y_train)
cat_model.fit(X_train, y_train)
lgbm_model.fit(X_train, y_train)

# Predictions
xgb_pred = xgb_model.predict(X_test)
cat_pred = cat_model.predict(X_test)
lgbm_pred = lgbm_model.predict(X_test)

# Hybrid Model
final_pred = (xgb_pred + cat_pred + lgbm_pred) / 3

# Evaluation
print('Hybrid Model R2:', r2_score(y_test, final_pred))
print('Hybrid Model RMSE:', np.sqrt(mean_squared_error(y_test, final_pred)))




# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split, RandomizedSearchCV
# from sklearn.metrics import r2_score, mean_squared_error
# from sklearn.preprocessing import StandardScaler
# from sklearn.ensemble import StackingRegressor
# from sklearn.linear_model import Ridge

# from xgboost import XGBRegressor
# from catboost import CatBoostRegressor
# from lightgbm import LGBMRegressor

# # Load dataset
# data = pd.read_csv('../data/insurance.csv')

# # Preprocessing
# data = pd.get_dummies(data, drop_first=True)
# X = data.drop('charges', axis=1)
# y = data['charges']

# # Feature scaling (optional, good for hybrid models)
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# # --- Hyperparameter tuning for XGBoost ---
# xgb_params = {
#     'n_estimators': [100, 200],
#     'max_depth': [3, 5, 6],
#     'learning_rate': [0.05, 0.1, 0.1],
#     'subsample': [0.8, 1.0]
# }

# xgb_search = RandomizedSearchCV(XGBRegressor(), xgb_params, n_iter=5, cv=3, scoring='r2', verbose=0)
# xgb_search.fit(X_train, y_train)
# xgb_model = xgb_search.best_estimator_

# # --- CatBoost ---
# cat_model = CatBoostRegressor(iterations=200, learning_rate=0.1, verbose=0)
# cat_model.fit(X_train, y_train)

# # --- LightGBM ---
# lgbm_model = LGBMRegressor(n_estimators=200, learning_rate=0.1)
# lgbm_model.fit(X_train, y_train)

# # --- Individual Predictions ---
# xgb_pred = xgb_model.predict(X_test)
# cat_pred = cat_model.predict(X_test)
# lgbm_pred = lgbm_model.predict(X_test)

# # --- Weighted Hybrid Prediction ---
# final_pred = (0.4 * xgb_pred) + (0.3 * cat_pred) + (0.3 * lgbm_pred)

# # --- Evaluation of Hybrid ---
# print("🔮 Weighted Hybrid Model R2 Score:", r2_score(y_test, final_pred))
# print("📉 Weighted Hybrid Model RMSE:", np.sqrt(mean_squared_error(y_test, final_pred)))

# # --- Feature Importance (from XGBoost) ---
# importance = pd.Series(xgb_model.feature_importances_, index=X.columns)
# importance.sort_values(ascending=False).plot(kind='bar', figsize=(10, 5), title='Feature Importance (XGBoost)')
# plt.tight_layout()
# plt.show()

# # --- Stacking Regressor Ensemble ---
# stack_model = StackingRegressor(
#     estimators=[
#         ('xgb', xgb_model),
#         ('cat', cat_model),
#         ('lgbm', lgbm_model)
#     ],
#     final_estimator=Ridge()
# )

# stack_model.fit(X_train, y_train)
# stack_pred = stack_model.predict(X_test)

# # --- Evaluation of Stacked Model ---
# print("🤖 Stacked Ensemble R2 Score:", r2_score(y_test, stack_pred))
# print("📉 Stacked Ensemble RMSE:", np.sqrt(mean_squared_error(y_test, stack_pred)))
