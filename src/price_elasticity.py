import pandas as pd
import numpy as np

df = pd.read_csv("data/processed/pricing_features.csv")

# Calculate percentage changes
df["Price_Change_%"] = (
    df["Price"].pct_change() * 100
)

df["Demand_Change_%"] = (
    df["Demand"].pct_change() * 100
)

# Calculate price elasticity
df["Price_Elasticity"] = (
    df["Demand_Change_%"] /
    df["Price_Change_%"]
)

# Remove infinite and missing values
df["Price_Elasticity"] = (
    df["Price_Elasticity"]
    .replace([np.inf, -np.inf], np.nan)
)

elasticity = df["Price_Elasticity"].dropna()

print("Price elasticity analysis completed!")

print("\nAverage Price Elasticity:", elasticity.mean())
print("Minimum Price Elasticity:", elasticity.min())
print("Maximum Price Elasticity:", elasticity.max())

print("\nSample results:")
print(
    df[
        [
            "Price",
            "Demand",
            "Price_Change_%",
            "Demand_Change_%",
            "Price_Elasticity"
        ]
    ].head(10)
)

df.to_csv(
    "data/processed/price_elasticity.csv",
    index=False
)

print("\nSaved: data/processed/price_elasticity.csv")