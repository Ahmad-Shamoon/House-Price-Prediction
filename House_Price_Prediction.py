import streamlit as st
import joblib
import numpy as np


model = joblib.load("House Price Prediction.joblib")

st.title("House Price Prediction")


area = st.number_input("Enter the area of the house (in sq.ft):", min_value=500, max_value=5000, step=100)
bedrooms = st.number_input("Enter the number of bedrooms:", min_value=1, max_value=10, step=1)
age = st.number_input("Enter the age of the house (in years):", min_value=0, max_value=100, step=1)

if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, age]])
    prediction = model.predict(input_data)
    
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")
