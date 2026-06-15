import pandas as pd
import numpy as np

np.random.seed(42)

days = 365

temperature = np.random.randint(18, 35, days)
server_load = np.random.randint(40, 100, days)

power_usage = (
    temperature * 20 +
    server_load * 15 +
    np.random.randint(-100, 100, days)
)

cost = power_usage * 0.12
carbon = power_usage * 0.45

df = pd.DataFrame({
    "Temperature": temperature,
    "Server_Load": server_load,
    "Power_Usage": power_usage,
    "Cost": cost,
    "Carbon_Emission": carbon
})

df.to_csv("data/energy_data.csv", index=False)

print("Dataset Generated Successfully!")
