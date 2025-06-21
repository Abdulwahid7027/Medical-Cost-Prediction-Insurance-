import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_style('whitegrid')
sns.set_palette("husl")

# Load dataset
data = pd.read_csv('../data/insurance.csv')

# Preprocessing: Convert categorical variables to numeric for correlation
data_encoded = pd.get_dummies(data, drop_first=True)

# 1. Correlation Heatmap
plt.figure(figsize=(12, 10))
correlation_matrix = data_encoded.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='PuOr', center=0, square=True, fmt='.2f')
plt.title('Correlation Matrix of Insurance Dataset Features')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.close()

# 2. Bar Plot: Average Charges by Sex
plt.figure(figsize=(8, 6))
sns.barplot(x='sex', y='charges', data=data)
plt.title('Average Insurance Charges by Sex')
plt.xlabel('Sex')
plt.ylabel('Insurance Charges ($)')
plt.tight_layout()
plt.savefig('sex_vs_charges_barplot.png')
plt.close()

# 3. Scatter Plot: Age vs. Charges with Smoker Hue
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='charges', hue='smoker', size='bmi', data=data)
plt.title('Age vs. Insurance Charges by Smoking Status and BMI')
plt.xlabel('Age')
plt.ylabel('Insurance Charges ($)')
plt.tight_layout()
plt.savefig('age_vs_charges_scatter.png')
plt.close()

# 4. Bar Plot: Average Charges by Number of Children
plt.figure(figsize=(8, 6))
sns.barplot(x='children', y='charges', data=data)
plt.title('Average Insurance Charges by Number of Children')
plt.xlabel('Number of Children')
plt.ylabel('Insurance Charges ($)')
plt.tight_layout()
plt.savefig('children_vs_charges_barplot.png')
plt.close()

# 5. Pair Plot for Numeric Features
sns.pairplot(data, vars=['age', 'bmi', 'charges'], hue='smoker', diag_kind='hist')
plt.suptitle('Pair Plot of Numeric Features by Smoking Status', y=1.02)
plt.tight_layout()
plt.savefig('numeric_pairplot.png')
plt.close()

# 6. Facet Grid: Charges by Smoker and Region
g = sns.FacetGrid(data, col='region', row='smoker', height=4, aspect=1)
g.map(sns.histplot, 'charges', bins=15)
g.set_titles(col_template="{col_name} Region", row_template="Smoker: {row_name}")
g.set_axis_labels('Insurance Charges ($)', 'Count')
plt.tight_layout()
plt.savefig('facet_grid_smoker_region.png')
plt.close()