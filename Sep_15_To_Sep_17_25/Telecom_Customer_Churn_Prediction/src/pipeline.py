# src/pipeline.py
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from src.preprocessing import DataPreprocessor

def create_pipeline(model, smote_kwargs=None):
    
    # Returns a pipeline: Preprocessing -> SMOTE -> Model

    smote = SMOTE(random_state=42, **(smote_kwargs or {}))

    return Pipeline(steps=[
        ("preprocessor", DataPreprocessor()),
        ("smote", smote),
        ("model", model)
    ])
