import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load pricing recommendations
df = pd.read_csv("data/processed/pricing_recommendations.csv")

features = [
    "Demand",
    "Inventory Level",
    "Units Sold",
    "Units Ordered",
    "Price",
    "Discount",
    "Competitor Pricing"
]

X = df[features]
y = df["Recommended Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print("ML Price Recommendation Model trained successfully!")
print("Price Recommendation MAE:", mae)

print("\nSample predictions:")

for actual, predicted in zip(y_test.head(10), predictions[:10]):
    print(
        f"Actual: {actual:.2f} | "
        f"Predicted: {predicted:.2f}"
    )