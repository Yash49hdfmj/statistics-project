import pandas as pd
import numpy as np
from sklearn.linear_model import RidgeCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import joblib

# Load cleaned data
df = pd.read_csv('../data/housing_clean.csv')
X = df.drop('SalePrice', axis=1)
y = df['SalePrice']

# Create pipeline
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('ridge', RidgeCV(alphas=np.logspace(-3, 3, 100), cv=5))
])

pipeline.fit(X, y)
joblib.dump(pipeline, '../model/final_pipeline.pkl')
print("✅ Model pipeline trained and saved as final_pipeline.pkl")
