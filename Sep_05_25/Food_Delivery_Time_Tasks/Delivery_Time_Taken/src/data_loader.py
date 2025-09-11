import pandas as pd

def load_data(path: str) -> pd.DataFrame:

    """Load raw CSV data."""
    
    return pd.read_csv(path)
