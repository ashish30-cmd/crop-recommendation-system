import streamlit as st
import pandas as pd
import joblib
model = joblib.load("model.pkl")
label_encoder = joblib.load("encoder.pkl")

st.set_page_config(page_title="Crop Recommendation", layout="centered")

st.title("Crop Recommendation System")

st.write("Enter soil and environmental parameters o get a crop recommendation.")

with st.form("input_form"):

    col1, col2 = st.columns(2)

    with col1:
        N = st.number_input("Nitrogen (N)", min_value=0, max_value=150, value=90)
        P = st.number_input("Phosphorus (P)", min_value=0, max_value=150, value=42)
        K = st.number_input("Potassium (K)", min_value=0, max_value=150, value=43)
        temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=22.0)

    with col2:
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=80.0)
        ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, value=6.5)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, value=200.0)

    submit = st.form_submit_button("Predict")
if submit:
    input_data = pd.DataFrame(
        [[N, P, K, temperature, humidity, ph, rainfall]],
        columns=["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
    )

    prediction = model.predict(input_data)
    crop = label_encoder.inverse_transform(prediction)

    st.success(f"Recommended Crop: {crop[0]}")