from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import category_encoders as ce  # Target/Frequency Encoder

def build_preprocessor(X):
    """Creates ColumnTransformer with OneHot + Target Encoding + Scaling."""
    categorical_low = ['transmission', 'fuel_type', 'drivetrain', 'body_type', 'seller_type']
    categorical_high = ['make', 'model', 'trim', 'exterior_color', 'interior_color']
    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

    # Remove already encoded / target columns if present
    numeric_features = [col for col in numeric_features if col not in ["price_log"]]

    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", RobustScaler())
    ])

    categorical_low_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    categorical_high_transformer = Pipeline(steps=[
        ("target_encoder", ce.TargetEncoder())
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat_low", categorical_low_transformer, categorical_low),
            ("cat_high", categorical_high_transformer, categorical_high)
        ]
    )

    return preprocessor


def build_pipeline(preprocessor, model):
    """Creates final pipeline with preprocessing + model."""
    return Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ])
