import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, RobustScaler
from sklearn.impute import SimpleImputer

def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    """Clean NaN variants and fix datatypes for delivery dataset."""
    df = df.replace(r'^\s*NaN\s*$', np.nan, regex=True)
    df = df.replace(r'^\s*$', np.nan, regex=True)

    # Convert numeric fields
    df['Delivery_person_Age'] = pd.to_numeric(df['Delivery_person_Age'], errors='coerce')
    df['multiple_deliveries'] = pd.to_numeric(df['multiple_deliveries'], errors='coerce')
    df['Delivery_person_Ratings'] = pd.to_numeric(df['Delivery_person_Ratings'], errors='coerce')
    df['multiple_deliveries'] = pd.to_numeric(df['multiple_deliveries'], errors='coerce')
    df['Weatherconditions'] = df['Weatherconditions'].fillna("Clear")


    # Festival column to binary
    df['Festival'] = df['Festival'].fillna("No Festival")
    df['Festival'] = df['Festival'].map({"Yes": 1, "No": 0})


    # Removing "(min)" from "Time_taken(min)"
    if "Time_taken(min)" in df.columns:
        if df["Time_taken(min)"].dtype == object:
            # If values are strings like "45 (min)"
            df["Time_taken(min)"] = df["Time_taken(min)"].str.replace("(min)", "", regex=False).str.strip().astype(int)
        else:
            # If already numeric, just ensure integer type
            df["Time_taken(min)"] = pd.to_numeric(df["Time_taken(min)"], errors='coerce').astype(int)
    else:
        print("Column 'Time_taken(min)' not found in DataFrame!")


    # Format date
    df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')

    # Format time columns as "HH:MM:SS"
    df['Time_Orderd'] = pd.to_datetime(df['Time_Orderd'], errors='coerce').dt.strftime('%H:%M:%S')
    df['Time_Order_picked'] = pd.to_datetime(df['Time_Order_picked'], errors='coerce').dt.strftime('%H:%M:%S')

    return df

def build_preprocessor(numeric_features, categorical_features):

    """Reusable preprocessing pipeline with imputation + scaling/encoding."""
    numeric_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_features),
            ("cat", categorical_pipeline, categorical_features)
        ]
    )
    return preprocessor
