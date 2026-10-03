import pandas as pd
import numpy as np
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error

print("Loading pricing data...")

df = pd.read_csv("data/processed/pricing_features.csv")

# Features used to predict demand
features = [
    "Inventory Level",
    "Units Sold",
    "Units Ordered",
    "Price",
    "Discount",
    "Competitor Pricing"
]

X = df[features].values
y = df["Demand"].values

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Scale features for neural network
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("Building TensorFlow model...")

# Simple neural network
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(len(features),)),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1)
])

model.compile(
    optimizer="adam",
    loss="mse"
)

# Train model
model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=32,
    verbose=1
)

# Make predictions
predictions = model.predict(X_test, verbose=0).flatten()

# Calculate error
mae = mean_absolute_error(y_test, predictions)

print("\nTensorFlow model trained successfully!")
print("TensorFlow Demand MAE:", mae)

print("\nSample predictions:")

for actual, predicted in zip(y_test[:10], predictions[:10]):
    print(
        f"Actual Demand: {actual:.0f} | "
        f"Predicted Demand: {predicted:.2f}"
    )