import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


# 1. Load dataset
df = pd.read_csv("data/raw/pricing_data.csv")

# 2. Select features
features = [
    "Inventory Level",
    "Units Sold",
    "Units Ordered",
    "Price",
    "Discount",
    "Competitor Pricing",
    "Demand"
]

X = df[features]
y = df["Price"]

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Create model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# 5. Train
model.fit(X_train, y_train)

# 6. Predict
predictions = model.predict(X_test)

# 7. Check accuracy
mae = mean_absolute_error(y_test, predictions)

print("Model trained successfully!")
print("Mean Absolute Error:", mae)