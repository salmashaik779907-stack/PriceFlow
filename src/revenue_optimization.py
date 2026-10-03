import pandas as pd

df = pd.read_csv("data/processed/pricing_recommendations.csv")

# Calculate revenue at current price
df["Current Revenue"] = df["Price"] * df["Units Sold"]

# Calculate revenue at recommended price
df["Recommended Revenue"] = (
    df["Recommended Price"] * df["Units Sold"]
)

# Calculate revenue difference
df["Revenue Difference"] = (
    df["Recommended Revenue"] - df["Current Revenue"]
)

print("Revenue optimization completed!")

print("\nSample results:")
print(
    df[
        [
            "Product ID",
            "Price",
            "Recommended Price",
            "Units Sold",
            "Current Revenue",
            "Recommended Revenue",
            "Revenue Difference"
        ]
    ].head(10)
)

print("\nTotal Current Revenue:",
      round(df["Current Revenue"].sum(), 2))

print("Total Recommended Revenue:",
      round(df["Recommended Revenue"].sum(), 2))

print("Potential Revenue Difference:",
      round(df["Revenue Difference"].sum(), 2))

df.to_csv(
    "data/processed/revenue_optimization.csv",
    index=False
)

print("\nSaved: data/processed/revenue_optimization.csv")