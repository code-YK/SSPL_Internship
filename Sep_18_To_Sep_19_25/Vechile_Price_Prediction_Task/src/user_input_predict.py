import pandas as pd
import numpy as np
import joblib
import os

# Import your functions from src folder
from src.data_prep import clean_data, feature_engineering 

# Path to trained pipeline/model
MODEL_PATH = os.path.join("models", "xgb_model.pkl")  # Change to your desired model file

# Load the trained pipeline
try:
    trained_pipeline = joblib.load(MODEL_PATH)
    print(f"Loaded trained model from {MODEL_PATH}")
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

# Function to get categorical input safely with choices
def get_categorical_input(prompt, choices):
    print(f"{prompt} (Choose from: {', '.join(choices)})")
    value = input("> ").strip()
    while value not in choices:
        print(f"Invalid input. Please choose from: {', '.join(choices)}")
        value = input("> ").strip()
    return value

# Define available options (you can pull from dataset if needed)
make_choices = ['Volkswagen', 'Lexus', 'Subaru', 'Cadillac', 'Toyota', 'Land Rover', 
                'Mazda', 'Ram', 'Chrysler', 'GMC', 'Volvo', 'Audi', 'Chevrolet', 'Tesla', 
                'Hyundai', 'Ford', 'Porsche', 'Acura', 'Nissan', 'Kia', 'Jeep', 'BMW', 'Dodge', 
                'Mercedes-Benz', 'Honda']
transmission_choices = ["Automatic", "Manual"]
fuel_choices = ["Petrol", "Diesel", "Electric", "Hybrid"]
drivetrain_choices = ["FWD", "RWD", "AWD"]
body_type_choices = ['Sedan', 'SUV', 'Hatchback', 'Pickup Truck', 'Coupe', 'Minivan', 'Wagon']
exterior_color_choices = ['Blue', 'Silver', 'Black', 'Red', 'White', 'Gray']
interior_color_choices = ['Brown', 'Beige', 'Gray', 'Black']
accident_choices = ['Major', 'Minor', 'No Accident']
condition_choices = ["Excellent", "Good", "Fair"]
seller_choices = ["Dealer", "Private"]
trim_choices = ['EX', 'LX', 'Touring', 'Base', 'Sport', 'Limited']

print("\nEnter Vehicle Details for Price Prediction:")

# Collect user inputs
vehicle_data = {
    "make": get_categorical_input("Enter Make", make_choices),
    "model": input("Enter Model: ").capitalize(),
    "transmission": get_categorical_input("Enter Transmission", transmission_choices),
    "fuel_type": get_categorical_input("Enter Fuel Type", fuel_choices),
    "drivetrain": get_categorical_input("Enter Drivetrain", drivetrain_choices),
    "body_type": get_categorical_input("Enter Body Type : ", body_type_choices),
    "exterior_color": get_categorical_input("Enter Exterior Color", exterior_color_choices),
    "interior_color": get_categorical_input("Enter Interior Color", interior_color_choices),
    "owner_count": int(input("Enter Number of Owners: ")),
    "accident_history": get_categorical_input("Accident History?", accident_choices),
    "seller_type": get_categorical_input("Seller Type", seller_choices),
    "condition": get_categorical_input("Vehicle Condition", condition_choices),
    "trim": get_categorical_input("Enter Trim : ", trim_choices),
    "vehicle_age": int(input("Enter Vehicle Age (in years): ")),
    "mileage": float(input("Enter Mileage (in km): ")),
    "engine_hp": float(input("Enter Engine HP: ")),
    "brand_popularity": float(input("Enter Brand Popularity Score (0-10): "))
}

# Convert to DataFrame
input_df = pd.DataFrame([vehicle_data])

# Preprocess data using your data_prep module
try:
    processed_df = clean_data(input_df)
    processed_df = feature_engineering(processed_df)
    print("Data preprocessed successfully.")
except Exception as e:
    print(f"Error in preprocessing: {e}")
    exit(1)

# Predict using trained pipeline
try:
    predicted_log_price = trained_pipeline.predict(processed_df)
    predicted_price = np.exp(predicted_log_price[0])
    print(f"\nPredicted Vehicle Price: {predicted_price:,.2f}")
except Exception as e:
    print(f"Error during prediction: {e}")
