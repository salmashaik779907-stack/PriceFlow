import pandas as pd

df = pd.read_csv("data/processed/inventory_adjusted_pricing.csv")


def competitor_adjustment(row):
    price = row["Inventory Adjusted Price"]
    competitor_price = row["Competitor Pricing"]

    # Our price is much higher than competitor
    if price > competitor_price * 1.10:
        price = competitor_price * 1.10

    # Our price is much lower than competitor
    elif price < competitor_price * 0.90:
        price = competitor_price * 0.90

    return round(price, 2)


df["Final Recommended Price"] = df.apply(
    competitor_adjustment,
    axis=1
)

print("Competitor price integration completed!")

print("\nSample results:")
print(
    df[
        [
            "Product ID",
            "Competitor Pricing",
            "Inventory Adjusted Price",
            "Final Recommended Price"
        ]
    ].head(10)
)

df.to_csv(
    "data/processed/final_pricing.csv",
    index=False
)

print("\nSaved: data/processed/final_pricing.csv")