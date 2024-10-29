import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

## load the model
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
scaler_model = pickle.load(open('models/scaler.pkl', 'rb'))

## set app title
st.title('Algerian Forest Fire Prediction')

st.write("Enter the values below to predict:")

# Input fields
temperature = st.number_input("Temperature", min_value=0.0, max_value=50.0, value=29.0, step=0.1)
rh = st.number_input("Relative Humidity (RH)", min_value=0, max_value=100, value=57, step=1)
ws = st.number_input("Wind Speed (Ws)", min_value=0.0, max_value=50.0, value=18.0, step=0.1)
rain = st.number_input("Rainfall (Rain)", min_value=0.0, max_value=50.0, value=0.0, step=0.1)
ffmc = st.number_input("Fine Fuel Moisture Code (FFMC)", min_value=0.0, max_value=100.0, value=65.7, step=0.1)
dmc = st.number_input("Duff Moisture Code (DMC)", min_value=0.0, max_value=100.0, value=3.4, step=0.1)
isi = st.number_input("Initial Spread Index (ISI)", min_value=0.0, max_value=50.0, value=0.3, step=0.1)

# Dropdowns for categorical data with conversion
classes = st.selectbox("Classes", ["Fire", "Not Fire"])
classes_numeric = 1 if classes == "Fire" else 0

region = st.selectbox("Region", ["Bijaya Region", "Sidi Bell Region"])
region_numeric = 1 if region == "Bijaya Region" else 0

# Prepare the input data for prediction
input_data = pd.DataFrame({
    'Temperature': [temperature],
    'RH': [rh],
    'Ws': [ws],
    'Rain': [rain],
    'FFMC': [ffmc],
    'DMC': [dmc],
    'ISI': [isi],
    'Classes': [classes_numeric],
    'Region': [region_numeric]
})

# Predict button
if st.button("Predict"):
    scaled_data = scaler_model.transform(input_data)
    fwi_prediction = ridge_model.predict(scaled_data)[0]  # Access the first (and only) element
    
    # Display FWI prediction beautifully
    st.markdown("<h2 style='text-align: center; color: green;'>Fire Weather Index (FWI) Prediction</h2>", unsafe_allow_html=True)
    st.metric(label="🔥 FWI Value", value=f"{fwi_prediction:.2f}")
    st.success(f"Predicted FWI: {fwi_prediction:.2f}")



