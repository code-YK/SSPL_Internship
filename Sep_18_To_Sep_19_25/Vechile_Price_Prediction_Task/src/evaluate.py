from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(model, X_test, y_test):
    """Computes regression metrics on test set."""
    preds = model.predict(X_test)
    
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    mape = np.mean(np.abs((y_test - preds) / y_test)) * 100  # Mean Absolute Percentage Error
    return pd.DataFrame([{"RMSE": rmse, "MAE": mae, "R2": r2, "MAPE": mape}])


def reg_graph(model, X_test, y_test):
    """Plots predicted vs actual values."""
    preds = model.predict(X_test)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=y_test, y=preds)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title(f"Predicted vs Actual Values for {type(model.named_steps['model']).__name__}")
    plt.show()