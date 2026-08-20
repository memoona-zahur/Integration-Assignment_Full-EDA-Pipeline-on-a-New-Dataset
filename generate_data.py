"""
Generate the orders dataset from the exact assignment spec.
Run this first to create orders_raw.csv.

Do not modify this script — the hidden grading checklist depends on
every trainee's dataset having the same shape and the same problems.
"""

import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=42)
n = 5000

orders = pd.DataFrame({
    "order_id": np.arange(1, n + 1),
    "order_date": pd.date_range("2024-01-01", periods=n, freq="h"),
    "customer_id": rng.integers(1000, 1200, size=n),
    "product_category": rng.choice(
        ["Electronics", "electronics", "Home Goods", "Apparel", "Books"], size=n
    ),
    "quantity": rng.integers(1, 8, size=n),
    "unit_price": rng.normal(45, 20, size=n).round(2),
    "region": rng.choice(
        ["North", "South", "East", "West", None],
        size=n, p=[0.24, 0.24, 0.24, 0.24, 0.04]
    ),
})

# Introduce the mess, on purpose — do not skip this part
orders.loc[rng.choice(n, 150, replace=False), "customer_id"] = None
orders.loc[rng.choice(n, 30, replace=False), "quantity"] *= -1
orders.loc[rng.choice(n, 20, replace=False), "unit_price"] = 4999.99
orders = pd.concat([orders, orders.sample(15, random_state=1)])

orders.to_csv("orders_raw.csv", index=False)
print(f"Saved orders_raw.csv — shape: {orders.shape}")
