import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Title
st.title("AI Data Center Energy Dashboard")

# Load Data
df = pd.read_csv("data/energy_data.csv")

# Load Model
model = joblib.load("models/energy_model.pkl")

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Power Usage Trend
st.subheader("Power Usage Trend")
fig, ax = plt.subplots()
ax.plot(df["Power_Usage"])
ax.set_xlabel("Days")
ax.set_ylabel("Power Usage")
st.pyplot(fig)

# Cost Trend
st.subheader("Cost Trend")
st.line_chart(df["Cost"])

# Carbon Emission Trend
st.subheader("Carbon Emission Trend")
st.line_chart(df["Carbon_Emission"])

# Prediction Section
st.subheader("Predict Power Usage")

temperature = st.slider(
    "Temperature (°C)",
    min_value=20,
    max_value=50,
    value=30
)

server_load = st.slider(
    "Server Load (%)",
    min_value=10,
    max_value=100,
    value=50
)

prediction = model.predict([[temperature, server_load]])

st.success(
    f"Predicted Power Usage: {prediction[0]:.2f} kWh"
)

# Footer
st.markdown("---")
st.write("Built with Python, Machine Learning, and Streamlit")
