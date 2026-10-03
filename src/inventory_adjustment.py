import pandas as pd

df = pd.read_csv("data/processed/pricing_recommendations.csv")


def adjust_price(row):
    price = row["Recommended Price"]
    inventory = row["Inventory Level"]
    demand = row["Demand"]

    # Very low inventory + high demand
    if inventory < 50 and demand > 100:
        price *= 1.08

    # High inventory + low demand
    elif inventory > 200 and demand < 80:
        price *= 0.92

    # Moderate inventory pressure
    elif inventory < 80:
        price *= 1.04

    return round(price, 2)


df["Inventory Adjusted Price"] = df.apply(
    adjust_price,
    axis=1
)

print("Inventory adjustment completed!")

print("\nSample results:")
print(
    df[
        [
            "Product ID",
            "Demand",
            "Inventory Level",
            "Recommended Price",
            "Inventory Adjusted Price"
        ]
    ].head(10)
)

df.to_csv(
    "data/processed/inventory_adjusted_pricing.csv",
    index=False
)

print("\nSaved: data/processed/inventory_adjusted_pricing.csv")
