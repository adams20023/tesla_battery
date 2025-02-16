import pandas as pd
import numpy as np

# Constants for current Tesla Model S Long Range
battery_capacity_kwh = 100  # kWh
energy_consumption_kwh_per_mile = 0.227  # kWh/mile (based on 440 miles range)

# Calculate current range
current_range_miles = battery_capacity_kwh / energy_consumption_kwh_per_mile

# Simulate driving conditions
np.random.seed(42)
num_samples = 1000
data = {
    "speed_mph": np.random.uniform(50, 80, num_samples),  # Speed in mph
    "temperature_c": np.random.uniform(-10, 40, num_samples),  # Temperature in Celsius
    "terrain": np.random.choice(["flat", "hilly"], num_samples),  # Terrain type
    "energy_consumption_kwh_per_mile": np.random.normal(0.227, 0.02, num_samples)  # kWh/mile
}

df = pd.DataFrame(data)

# Add range column
df["range_miles"] = battery_capacity_kwh / df["energy_consumption_kwh_per_mile"]

# Save to CSV
df.to_csv("current_battery_performance.csv", index=False)
print(f"Simulated current Tesla range: {current_range_miles:.2f} miles")
