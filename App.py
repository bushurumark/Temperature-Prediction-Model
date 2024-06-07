#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install streamlit


# In[2]:


import streamlit as st
import joblib
import numpy as np

# Load the pre-trained model
model = joblib.load("model.pkl")

# Define the prediction function
def predict_temperature(features):
    return model.predict([features])[0]

st.markdown(
    """
    <style>
    .title {
        color: #4CAF50;
        text-align: center;
    }
    .header {
        color: #f39c12;
        margin-top: 20px;
    }
    .result {
        color: #27ae60;
        font-size: 24px;
        margin-top: 20px;
    }
    .error {
        color: #e74c3c;
        font-size: 24px;
        margin-top: 20px;
    }
    body {
        background-color: #3498db; /* Background color set to blue */
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title'>Temperature Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='header'>Input Parameters</h2>", unsafe_allow_html=True)
# Define the input fields
energy_delta = st.number_input("Energy delta[Wh]", value=0.0)
ghi = st.number_input("Global Horizontal Irradiance", value=0.0)
pressure = st.number_input("Pressure", value=1013.25)
humidity = st.number_input("Humidity", value=50.0)
wind_speed = st.number_input("Wind speed", value=0.0)
rain_1h = st.number_input("Rain", value=0.0)
snow_1h = st.number_input("Snow", value=0.0)
clouds_all = st.number_input("Clouds", value=0.0)
Sun_levels = {0: 'Not Sunny', 1: 'Sunny'}
options = [f"{key}-{value}" for key, value in Sun_levels.items()]
is_sun = st.selectbox('Availability of Sun', options)
sunlight_time = st.number_input("Sun Light Time", value=0.0)
day_length = st.number_input("Day Length", value=0.0)
sunlight_ratio = st.number_input("Sunlight Time/Day Length", value=0.0)
Type_levels = {1: 'Clear', 2: 'Clouds', 3: 'Rain', 4: 'Snow', 5: 'Other'}
options = [f"{key}-{value}" for key, value in Type_levels.items()]
weather_type = st.selectbox('Weather Type', options)
hour = st.number_input("Hour", min_value=0, max_value=23, value=0)
month = st.number_input("Month", min_value=1, max_value=12, value=1)

# Prepare the features for prediction
features = [
    energy_delta, ghi, pressure, humidity, wind_speed, rain_1h, snow_1h, clouds_all,
    is_sun, sunlight_time, day_length, sunlight_ratio, weather_type, hour, month
]

# Button to make predictions
if st.button("Predict Temperature"):
    prediction = predict_temperature(features)
    st.markdown(f"<div class='result'>The predicted temperature is {prediction:.2f} °C</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='error'>Click the button to predict the temperature</div>", unsafe_allow_html=True)

