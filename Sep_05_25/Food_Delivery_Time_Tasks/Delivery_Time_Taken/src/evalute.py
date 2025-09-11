from sklearn.metrics import mean_absolute_error, mean_squared_error, accuracy_score

def print_scores(model, X_train, y_train, X_test, y_test):

    print("Train MAE:", mean_absolute_error(y_train, model.predict(X_train)))
    print("Test MAE:", mean_absolute_error(y_test, model.predict(X_test)))
    print("Train MSE:", mean_squared_error(y_train, model.predict(X_train)))
    print("Test MSE:", mean_squared_error(y_test, model.predict(X_test)))
    print("Train R2:", model.score(X_train, y_train))
    print("Test R2:", model.score(X_test, y_test))