from sklearn.pipeline import Pipeline
from .preprocessing import build_preprocessor

def get_pipeline(model, numeric_features, categorical_features):
    """Return a full pipeline: preprocessing + model."""
    preprocessor = build_preprocessor(numeric_features, categorical_features)
    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("regressor", model)
    ])
    return pipeline
