# src/preprocessing.py
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

class DataPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.numeric_features = []
        self.categorical_features = []
        self.column_transformer = None

    def fit(self, X, y=None):
        X = X.copy()

        # Identify numeric vs categorical
        self.numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
        self.categorical_features = X.select_dtypes(include=['object', 'category']).columns.tolist()

        # Build transformers
        self.column_transformer = ColumnTransformer(transformers=[
            ("num", StandardScaler(), self.numeric_features),
            ("cat", OneHotEncoder(handle_unknown='ignore'), self.categorical_features)
        ])

        self.column_transformer.fit(X)
        return self

    def transform(self, X):
        X = X.copy()

        # Numeric imputation (median)
        for col in self.numeric_features:
            X[col] = X[col].fillna(X[col].median())

        # Categorical imputation (mode)
        for col in self.categorical_features:
            X[col] = X[col].fillna(X[col].mode()[0])

        return self.column_transformer.transform(X)
