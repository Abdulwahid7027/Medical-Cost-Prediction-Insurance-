import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor

# Set Seaborn style
sns.set_style('whitegrid')
sns.set_palette("husl")

# Load dataset
data = pd.read_csv('../data/insurance.csv')

# Preprocessing
data = pd.get_dummies(data, drop_first=True)
X = data.drop('charges', axis=1)
y = data['charges']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

# Initialize models
xgb_model = XGBRegressor(n_estimators=75, learning_rate=0.1)
cat_model = CatBoostRegressor(iterations=75, learning_rate=0.1, verbose=0)
lgbm_model = LGBMRegressor(n_estimators=75, learning_rate=0.1)

# Fit models
xgb_model.fit(X_train, y_train)
cat_model.fit(X_train, y_train)
lgbm_model.fit(X_train, y_train)

# Predictions
xgb_pred = xgb_model.predict(X_test)
cat_pred = cat_model.predict(X_test)
lgbm_pred = lgbm_model.predict(X_test)

# Hybrid Model Predictions (average of the three)
hybrid_pred = (xgb_pred + cat_pred + lgbm_pred) / 3

# Calculate metrics
xgb_r2 = r2_score(y_test, xgb_pred)
xgb_rmse = np.sqrt(mean_squared_error(y_test, xgb_pred))
hybrid_r2 = r2_score(y_test, hybrid_pred)
hybrid_rmse = np.sqrt(mean_squared_error(y_test, hybrid_pred))
xgb_mae = mean_absolute_error(y_test, xgb_pred)
hybrid_mae = mean_absolute_error(y_test, hybrid_pred)

# 1. Bar Plot: R² and RMSE Comparison (Separate Subplots)
metrics_r2 = pd.DataFrame({
    'Model': ['XGBoost', 'Hybrid'],
    'Metric': ['R²', 'R²'],
    'Value': [xgb_r2, hybrid_r2]
})
metrics_rmse = pd.DataFrame({
    'Model': ['XGBoost', 'Hybrid'],
    'Metric': ['RMSE', 'RMSE'],
    'Value': [xgb_rmse, hybrid_rmse]
})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
# R² subplot
r2_plot = sns.barplot(x='Metric', y='Value', hue='Model', data=metrics_r2, ax=ax1)
ax1.set_title('R² Comparison: XGBoost vs. Hybrid Model')
ax1.set_ylabel('R² Score')
ax1.set_ylim(0, 1.05)  # Fixed scale for R² (0 to 1.05)
for p in r2_plot.patches:
    r2_plot.annotate(f'{p.get_height():.4f}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=10)
# RMSE subplot
rmse_plot = sns.barplot(x='Metric', y='Value', hue='Model', data=metrics_rmse, ax=ax2)
ax2.set_title('RMSE Comparison: XGBoost vs. Hybrid Model')
ax2.set_ylabel('RMSE ($)')
ax2.set_ylim(0, max(xgb_rmse, hybrid_rmse) * 1.1)  # Dynamic scale for RMSE
for p in rmse_plot.patches:
    rmse_plot.annotate(f'{p.get_height():.2f}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.savefig('model_performance_barplot.png')
plt.close()

# 2. Scatter Plot: Actual vs. Predicted Charges
plt.figure(figsize=(10, 6))
plt.scatter(y_test, xgb_pred, label='XGBoost', alpha=0.5, colowr='blue')
plt.scatter(y_test, hybrid_pred, label='Hybrid', alpha=0.5, color='orange')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('Actual Charges ($)')
plt.ylabel('Predicted Charges ($)')
plt.title('Actual vs. Predicted Charges: XGBoost vs. Hybrid Model')
plt.legend()
plt.tight_layout()
plt.savefig('actual_vs_predicted_scatter.png')
plt.close()

# 3. Bar Plot: Mean Absolute Error Comparison
mae_data = pd.DataFrame({
    'Model': ['XGBoost', 'Hybrid'],
    'MAE': [xgb_mae, hybrid_mae]
})
plt.figure(figsize=(8, 6))
mae_plot = sns.barplot(x='Model', y='MAE', data=mae_data)
plt.title('Mean Absolute Error: XGBoost vs. Hybrid Model')
plt.ylabel('Mean Absolute Error ($)')
for p in mae_plot.patches:
    mae_plot.annotate(f'{p.get_height():.2f}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.savefig('mae_comparison_barplot.png')
plt.close()