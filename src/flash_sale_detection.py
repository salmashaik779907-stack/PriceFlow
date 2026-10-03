import pandas as pd

# Load pricing data
df = pd.read_csv("data/raw/pricing_data.csv")

print("Flash Sale Detection Started!")
print("=" * 50)

# Calculate average demand
average_demand = df["Demand"].mean()

print(f"Average Demand: {average_demand:.2f}")

print("\nChecking products...\n")

# Check first 20 products
for _, row in df.head(20).iterrows():

    demand = row["Demand"]
    inventory = row["Inventory Level"]

    # Flash sale condition
    if demand > average_demand * 1.5 and inventory < 150:
        status = "🔥 POSSIBLE FLASH SALE"

    else:
        status = "Normal"

    print(
        f"Product: {row['Product ID']} | "
        f"Demand: {demand} | "
        f"Inventory: {inventory} | "
        f"Status: {status}"
    )

print("\nFlash sale detection completed!")