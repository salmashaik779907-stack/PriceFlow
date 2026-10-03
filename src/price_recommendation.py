import pandas as pd

df = pd.read_csv("data/processed/pricing_features.csv")

def recommend_price(row):
    current_price = row["Price"]
    competitor_price = row["Competitor Pricing"]
    demand = row["Demand"]
    inventory = row["Inventory Level"]

    # Start with current price
    recommended_price = current_price

    # High demand + low inventory → increase price
    if demand > 120 and inventory < 100:
        recommended_price *= 1.10

    # Low demand + high inventory → decrease price
    elif demand < 80 and inventory > 150:
        recommended_price *= 0.90

    # Keep price reasonably close to competitor price
    if recommended_price > competitor_price * 1.15:
        recommended_price = competitor_price * 1.15

    if recommended_price < competitor_price * 0.85:
        recommended_price = competitor_price * 0.85

    return round(recommended_price, 2)


df["Recommended Price"] = df.apply(recommend_price, axis=1)

print("Price recommendation completed!")

print("\nSample recommendations:")
print(
    df[
        [
            "Product ID",
            "Price",
            "Competitor Pricing",
            "Demand",
            "Inventory Level",
            "Recommended Price",
        ]
    ].head(10)
)

df.to_csv(
    "data/processed/pricing_recommendations.csv",
    index=False
)

print("\nSaved: data/processed/pricing_recommendations.csv")