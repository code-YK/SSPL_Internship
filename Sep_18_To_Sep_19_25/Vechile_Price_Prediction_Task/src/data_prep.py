import pandas as pd
import numpy as np

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Handles missing values, drops redundant columns, and standardizes data."""
    df = df.copy()
    
    # Drop redundant columns
    if "year" in df.columns:
        df.drop(columns=["year"], inplace=True)
    if "mileage_per_year" in df.columns:
        df.drop(columns=["mileage_per_year"], inplace=True)
    
    # Fill accident_history
    df["accident_history"] = df["accident_history"].fillna("No Accident")
    
    # Fill other categorical missing values with mode
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    # Fill numeric missing with median
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col] = df[col].fillna(df[col].median())
    
    return df


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """Adds engineered features like log(price), price_per_hp, luxury flag."""
    df = df.copy()
    
    # Log transform target
    df["price_log"] = np.log1p(df["price"])
    
    # Derived feature: price per HP
    if "price" in df.columns and "engine_hp" in df.columns:
        df["price_per_hp"] = df["price"] / df["engine_hp"].replace(0, np.nan)
        df["price_per_hp"].fillna(df["price_per_hp"].median(), inplace=True)
    
    # Luxury brand flag
    luxury_brands = ["BMW", "Mercedes-Benz", "Audi", "Lexus", "Jaguar", "Porsche"]
    df["is_luxury_brand"] = df["make"].apply(lambda x: 1 if x in luxury_brands else 0)
    
    # Condition encoding
    condition_map = {"Excellent": 3, "Good": 2, "Fair": 1}
    df["condition_encoded"] = df["condition"].map(condition_map).fillna(2)
    
    return df


def split_features_target(df: pd.DataFrame, target="price_log"):
    """Splits dataset into features (X) and target (y)."""
    X = df.drop(columns=["price", target])
    y = df[target]
    return X, y
