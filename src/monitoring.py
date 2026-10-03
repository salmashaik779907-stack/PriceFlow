import pandas as pd

# Load advanced pricing results
df = pd.read_csv("data/processed/advanced_pricing.csv")

print("Dynamic Pricing Monitoring System")
print("=" * 60)

average_demand = df["Demand"].mean()

alerts = []

for _, row in df.iterrows():

    product = row["Product ID"]
    demand = row["Demand"]
    inventory = row["Inventory Level"]
    current_price = row["Price"]
    recommended_price = row["Advanced Recommended Price"]

    # Flash-sale alert
    if demand > average_demand * 1.5 and inventory < 150:
        alerts.append(
            f"🔥 FLASH SALE: {product} | "
            f"Demand={demand}, Inventory={inventory}"
        )

    # Low inventory alert
    if inventory < 50:
        alerts.append(
            f"📦 LOW INVENTORY: {product} | "
            f"Inventory={inventory}"
        )

    # Large price-change alert
    price_change = abs(
        recommended_price - current_price
    ) / current_price * 100

    if price_change > 10:
        alerts.append(
            f"📈 LARGE PRICE CHANGE: {product} | "
            f"Change={price_change:.2f}%"
        )


print("\n🚨 SYSTEM ALERTS")
print("-" * 60)

if alerts:
    for alert in alerts[:30]:
        print(alert)
else:
    print("No critical alerts detected.")

print("\nTotal alerts generated:", len(alerts))

print("\nMonitoring completed!")