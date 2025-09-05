import numpy as np
import pandas as pd

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Compute Haversine distance in km.
    """
    R = 6371  # Earth radius (km)
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
    return 2 * R * np.arcsin(np.sqrt(a))

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add engineered features like distance, time gaps, temporal features.
    """
    df["distance_km"] = haversine_distance(
        df["Restaurant_latitude"], df["Restaurant_longitude"],
        df["Delivery_location_latitude"], df["Delivery_location_longitude"]
    )

    # Convert time strings to datetime for calculations
    order_time = pd.to_datetime(df['Time_Orderd'], format='%H:%M:%S', errors='coerce')
    pickup_time = pd.to_datetime(df['Time_Order_picked'], format='%H:%M:%S', errors='coerce')
 
    # New numeric features
    df["order_hour"] = order_time.dt.hour  # NaN if missing
    df["order_to_pickup_time"] = (pickup_time - order_time).dt.total_seconds() / 60

    # Create weekend indicator (Saturday=5, Sunday=6)
    df["is_weekend"] = df["Order_Date"].dt.dayofweek >= 5
    df["is_weekend"] = df["is_weekend"].astype(int)

    return df
