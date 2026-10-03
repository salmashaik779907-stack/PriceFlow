import pandas as pd

df = pd.read_csv("data/raw/pricing_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort by time
df = df.sort_values("Date")

# Use Date as the time index
df = df.set_index("Date")

# 5-day window with 1-day sliding step
rolling_demand = (
    df["Demand"]
    .rolling("5D")
    .mean()
)

df["Rolling_Average_Demand"] = rolling_demand

print("Sliding-window demand analysis completed!")

print("\nSample results:")
print(
    df[
        [
            "Product ID",
            "Demand",
            "Rolling_Average_Demand"
        ]
    ].head(10)
)

df.reset_index().to_csv(
    "data/processed/sliding_window_demand.csv",
    index=False
)

print("\nSaved: data/processed/sliding_window_demand.csv")