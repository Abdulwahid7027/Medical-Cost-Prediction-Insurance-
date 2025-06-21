import numpy as np
from scipy.stats import wilcoxon

# Simulated fold-wise metrics (same as above)
xgboost_r2 = np.array([0.865, 0.870, 0.867, 0.869, 0.868, 0.866, 0.871, 0.867, 0.868, 0.869])
hybrid_r2 = np.array([0.878, 0.882, 0.879, 0.881, 0.880, 0.879, 0.883, 0.880, 0.881, 0.882])
xgboost_rmse = np.array([4470, 4440, 4460, 4455, 4445, 4465, 4435, 4450, 4448, 4455])
hybrid_rmse = np.array([4325, 4300, 4315, 4305, 4310, 4320, 4295, 4310, 4308, 4305])

# Wilcoxon Signed-Rank Test for R²
stat_r2, p_value_r2 = wilcoxon(xgboost_r2, hybrid_r2, alternative='less')
# Wilcoxon Signed-Rank Test for RMSE
stat_rmse, p_value_rmse = wilcoxon(xgboost_rmse, hybrid_rmse, alternative='greater')

# Display results
print(f"R² Wilcoxon Statistic: {stat_r2:.1f}, p-Value: {p_value_r2:.5f}, Result: {'Significant Improvement' if p_value_r2 < 0.05 else 'Not Significant'}")
print(f"RMSE Wilcoxon Statistic: {stat_rmse:.1f}, p-Value: {p_value_rmse:.5f}, Result: {'Significant Reduction' if p_value_rmse < 0.05 else 'Not Significant'}")