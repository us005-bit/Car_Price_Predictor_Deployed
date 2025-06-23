import streamlit as st
import pickle
import numpy as np

# Load the trained polynomial regression model
with open('PolynomialModel.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Car Price Predictor")
st.subheader("Used Car Price Predictor - Polynomial Regression")
# --- Input Fields ---
present_price = st.number_input("Present Price (in Lakhs)", min_value=0.0, value=5.0)
kms_driven = st.number_input("Kilometers Driven", min_value=0, value=10000)
owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])
car_age = st.slider("Car Age (in Years)", min_value=0, max_value=30, value=5)
fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel'])

# --- Encoding ---
fuel_diesel = 1 if fuel_type == 'Diesel' else 0
fuel_petrol = 1 if fuel_type == 'Petrol' else 0

# --- Final Input (must match training order) ---
input_data = np.array([[present_price, kms_driven, owner, car_age, fuel_diesel, fuel_petrol]])

# --- Predict Button ---
if st.button("Predict Selling Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Selling Price: ₹ {round(prediction, 2)} Lakhs")
