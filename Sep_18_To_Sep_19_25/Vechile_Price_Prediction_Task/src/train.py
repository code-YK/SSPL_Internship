from sklearn.model_selection import train_test_split
import joblib

def stratified_split(X, y, stratify_col=None, test_size=0.2, random_state=42):
    """Performs stratified train-test split based on given column."""
    if stratify_col is not None:
        return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=stratify_col)
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def train_and_save_model(pipeline, X_train, y_train, model_path="models/saved_model.pkl"):
    """Fits pipeline on training data and saves."""
    pipeline.fit(X_train, y_train)
    joblib.dump(pipeline, model_path)
    print(f"Model saved to {model_path}")
    return pipeline
