import pandas as pd

df = pd.read_csv("C://Users//91810//Desktop//statistics-project//data//housing_clean.csv")  # Adjust path if needed

features = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF',
            '1stFlrSF', 'YearBuilt', 'FullBath', 'Fireplaces']

for col in features:
    print(f"//n🔹 {col} - Distinct Values:")
    print(df[col].dropna().unique())
