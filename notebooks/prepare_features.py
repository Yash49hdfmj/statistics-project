import pandas as pd

# Load original data
data = pd.read_csv('../data/train.csv')

# Select base features
features = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF',
            '1stFlrSF', 'YearBuilt', 'FullBath', 'Fireplaces']

# Add interaction term
data['GrLivArea_OverallQual'] = data['GrLivArea'] * data['OverallQual']
features.append('GrLivArea_OverallQual')

# Extract selected features and target
X = data[features]
y = data['SalePrice']

# Save clean version
clean_df = X.copy()
clean_df['SalePrice'] = y
clean_df.to_csv('../data/housing_clean.csv', index=False)
print("✅ Clean dataset saved as housing_clean.csv")
