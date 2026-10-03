import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/pricing_data.csv")

# -----------------------------
# Feature Engineering
# -----------------------------

# 1. Stock pressure
df["Stock_Pressure"] = df["Demand"] / (df["Inventory Level"] + 1)

# 2. Sales-to-inventory ratio
df["Sales_Inventory_Ratio"] = (
    df["Units Sold"] / (df["Inventory Level"] + 1)
)

# 3. Competitor price difference
df["Competitor_Price_Difference"] = (
    df["Price"] - df["Competitor Pricing"]
)

# 4. Competitor price percentage difference
df["Competitor_Price_Ratio"] = (
    df["Price"] / (df["Competitor Pricing"] + 1)
)

# 5. Discount amount
df["Discount_Amount"] = (
    df["Price"] * df["Discount"] / 100
)

# 6. Effective price after discount
df["Effective_Price"] = (
    df["Price"] - df["Discount_Amount"]
)

# Save processed dataset
df.to_csv(
    "data/processed/pricing_features.csv",
    index=False
)

print("Feature engineering completed!")
print("New shape:", df.shape)
print("\nNew features:")
print([
    "Stock_Pressure",
    "Sales_Inventory_Ratio",
    "Competitor_Price_Difference",
    "Competitor_Price_Ratio",
    "Discount_Amount",
    "Effective_Price"
])