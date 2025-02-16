import pandas as pd
import numpy as np

# Load current data
df = pd.read_csv("current_battery_performance.csv")

# Improved parameters
improved_battery_capacity_kwh = 180  # Increased battery capacity
improved_energy_consumption_kwh_per_mile = 0.125  # Reduced energy consumption

# Calculate improved range
improved_range_miles = improved_battery_capacity_kwh / improved_energy_consumption_kwh_per_mile

# Simulate improved driving conditions
np.random.seed(42)
num_samples = 1000
improved_data = {
    "speed_mph": np.random.uniform(40, 60, num_samples),  # Optimized speed
    "temperature_c": np.random.uniform(10, 30, num_samples),  # Moderate temperature
    "terrain": np.random.choice(["flat"], num_samples),  # Flat terrain only
    "energy_consumption_kwh_per_mile": np.random.normal(0.125, 0.01, num_samples)  # Reduced kWh/mile
}

improved_df = pd.DataFrame(improved_data)

# Add range column
improved_df["range_miles"] = improved_battery_capacity_kwh / improved_df["energy_consumption_kwh_per_mile"]

# Save to CSV
improved_df.to_csv("improved_battery_performance.csv", index=False)
print(f"Simulated improved Tesla range: {improved_range_miles:.2f} miles")
