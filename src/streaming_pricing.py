import pandas as pd
import time

# Load pricing data
df = pd.read_csv("data/raw/pricing_data.csv")

print("Real-Time Streaming Pricing Prototype")
print("=" * 60)

average_demand = df["Demand"].mean()

# Simulate incoming events
for _, row in df.head(20).iterrows():

    product = row["Product ID"]
    demand = row["Demand"]
    inventory = row["Inventory Level"]
    current_price = row["Price"]
    competitor_price = row["Competitor Pricing"]

    price = current_price

    # Demand + inventory adjustment
    if demand > 120 and inventory < 100:
        price *= 1.08

    elif demand < 80 and inventory > 200:
        price *= 0.92

    # Flash-sale detection
    flash_sale = (
        demand > average_demand * 1.5
        and inventory < 150
    )

    if flash_sale:
        price *= 1.05

    # Competitor influence
    price = (price * 0.70) + (competitor_price * 0.30)

    # Price limits
    maximum_price = competitor_price * 1.10
    minimum_price = competitor_price * 0.90

    price = max(min(price, maximum_price), minimum_price)

    price = round(price, 2)

    print("\n📡 Incoming Event")
    print("-" * 40)
    print(f"Product: {product}")
    print(f"Demand: {demand}")
    print(f"Inventory: {inventory}")
    print(f"Current Price: ₹{current_price:.2f}")
    print(f"Competitor Price: ₹{competitor_price:.2f}")

    if flash_sale:
        print("🔥 Flash Sale Detected!")

    print(f"⚡ New Recommended Price: ₹{price:.2f}")

    # Simulate streaming delay
    time.sleep(1)

print("\n" + "=" * 60)
print("Streaming pricing simulation completed!")