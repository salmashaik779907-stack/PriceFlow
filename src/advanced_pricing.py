import pandas as pd

# Load pricing data
df = pd.read_csv("data/raw/pricing_data.csv")

print("Advanced Dynamic Pricing Engine")
print("=" * 60)


def calculate_price(row):

    current_price = row["Price"]
    competitor_price = row["Competitor Pricing"]
    demand = row["Demand"]
    inventory = row["Inventory Level"]

    price = current_price

    # 1. Demand + inventory adjustment
    if demand > 120 and inventory < 100:
        price *= 1.08

    elif demand < 80 and inventory > 200:
        price *= 0.92

    # 2. Flash-sale adjustment
    average_demand = df["Demand"].mean()

    if demand > average_demand * 1.5 and inventory < 150:
        price *= 1.05

    # 3. Competitor price influence
    # 70% our calculated price + 30% competitor price
    price = (price * 0.70) + (competitor_price * 0.30)

    # 4. Keep price within reasonable competitor range
    maximum_price = competitor_price * 1.10
    minimum_price = competitor_price * 0.90

    if price > maximum_price:
        price = maximum_price

    elif price < minimum_price:
        price = minimum_price

    return round(price, 2)


# Generate final prices
df["Advanced Recommended Price"] = df.apply(
    calculate_price,
    axis=1
)

# Display results
print("\nSample Advanced Pricing Results:\n")

print(
    df[
        [
            "Product ID",
            "Demand",
            "Inventory Level",
            "Price",
            "Competitor Pricing",
            "Advanced Recommended Price"
        ]
    ].head(20).to_string(index=False)
)

# Save results
df.to_csv(
    "data/processed/advanced_pricing.csv",
    index=False
)

print("\nAdvanced pricing completed!")
print("Saved: data/processed/advanced_pricing.csv")