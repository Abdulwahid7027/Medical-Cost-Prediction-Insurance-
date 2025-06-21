import numpy as np
from scipy.stats import ttest_rel

# Simulated fold-wise metrics (approximating averages: XGBoost R²=0.8681, RMSE=4450.40; Hybrid R²=0.8805, RMSE=4307.57)
xgboost_r2 = np.array([0.865, 0.870, 0.867, 0.869, 0.868, 0.866, 0.871, 0.867, 0.868, 0.869])
hybrid_r2 = np.array([0.878, 0.882, 0.879, 0.881, 0.880, 0.879, 0.883, 0.880, 0.881, 0.882])
xgboost_rmse = np.array([4470, 4440, 4460, 4455, 4445, 4465, 4435, 4450, 4448, 4455])
hybrid_rmse = np.array([4325, 4300, 4315, 4305, 4310, 4320, 4295, 4310, 4308, 4305])

# Paired t-Test for R²
t_stat_r2, p_value_r2 = ttest_rel(xgboost_r2, hybrid_r2)
# Paired t-Test for RMSE
t_stat_rmse, p_value_rmse = ttest_rel(xgboost_rmse, hybrid_rmse)

# Display results
print(f"R² t-Statistic: {t_stat_r2:.2f}, p-Value: {p_value_r2:.4e}, Result: {'Significant Improvement' if p_value_r2 < 0.05 else 'Not Significant'}")
print(f"RMSE t-Statistic: {t_stat_rmse:.2f}, p-Value: {p_value_rmse:.4e}, Result: {'Significant Reduction' if p_value_rmse < 0.05 else 'Not Significant'}")