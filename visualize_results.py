import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
current_df = pd.read_csv("current_battery_performance.csv")
improved_df = pd.read_csv("improved_battery_performance.csv")

# Plot histograms of ranges
plt.figure(figsize=(12, 6))
sns.histplot(current_df["range_miles"], color="blue", label="Current Range (440 miles)", kde=True)
sns.histplot(improved_df["range_miles"], color="green", label="Improved Range (800 miles)", kde=True)
plt.title("Tesla Battery Range: Current vs Improved")
plt.xlabel("Range (miles)")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Print summary statistics
print("Current Range Summary:")
print(current_df["range_miles"].describe())
print("\nImproved Range Summary:")
print(improved_df["range_miles"].describe())
