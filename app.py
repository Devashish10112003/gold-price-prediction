import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('random_forest_model.pkl')

# Define the required input features
required_columns = [
    'SP_Ajclose', 'DJ_Ajclose', 'EG_Ajclose', 'EU_Price', 'OF_Price',
    'OS_Price', 'SF_Price', 'USB_Price', 'PLT_Price', 'PLD_Price',
    'RHO_PRICE', 'USDI_Price', 'GDX_Adj Close', 'USO_Adj Close'
]

# Streamlit UI
st.title("Gold Price Prediction App")
st.write("Enter the required values below to predict the gold price.")

# Create input fields dynamically
input_data = {}
for col in required_columns:
    input_data[col] = st.number_input(f"Enter {col}", value=0.0)

# Predict button
if st.button("Predict Price"):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])

    # Ensure all required columns exist
    for col in required_columns:
        if col not in input_df.columns:
            input_df[col] = 0  

    # Predict
    prediction = model.predict(input_df)[0]

    # Display result
    st.success(f"Predicted Gold Price: ${prediction:.2f}")
