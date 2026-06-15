import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("data/energy_data.csv")

X = df[["Temperature", "Server_Load"]]
y = df["Power_Usage"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "models/energy_model.pkl")

print("Model Trained Successfully!")
