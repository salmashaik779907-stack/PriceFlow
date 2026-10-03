import pandas as pd

df = pd.read_csv("data/processed/pricing_features.csv")

print("Average Demand:", df["Demand"].mean())
print("Minimum Demand:", df["Demand"].min())
print("Maximum Demand:", df["Demand"].max())

print("\nAverage Demand by Category:")
print(df.groupby("Category")["Demand"].mean().sort_values(ascending=False))

print("\nAverage Demand by Season:")
print(df.groupby("Seasonality")["Demand"].mean().sort_values(ascending=False))