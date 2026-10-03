import pandas as pd
import time

# Load pricing data
df = pd.read_csv("data/raw/pricing_data.csv")

print("Real-Time Dynamic Pricing Simulation Started!")
print("=" * 50)

# Simulate incoming product data
for index, row in df.head(10).iterrows():

    demand = row["Demand"]
    inventory = row["Inventory Level"]
    current_price = row["Price"]
    competitor_price = row["Competitor Pricing"]

    recommended_price = current_price

    # High demand + low inventory → increase price
    if demand > 120 and inventory < 100:
        recommended_price *= 1.08

    # Low demand + high inventory → decrease price
    elif demand < 80 and inventory > 200:
        recommended_price *= 0.92

    # Keep price close to competitor price
    if recommended_price > competitor_price * 1.10:
        recommended_price = competitor_price * 1.10

    elif recommended_price < competitor_price * 0.90:
        recommended_price = competitor_price * 0.90

    recommended_price = round(recommended_price, 2)

    print(f"\nProduct: {row['Product ID']}")
    print(f"Demand: {demand}")
    print(f"Inventory: {inventory}")
    print(f"Current Price: ₹{current_price:.2f}")
    print(f"Competitor Price: ₹{competitor_price:.2f}")
    print(f"Recommended Price: ₹{recommended_price:.2f}")

    print("-" * 50)

    # Simulate real-time delay
    time.sleep(1)

print("\nReal-time pricing simulation completed!")