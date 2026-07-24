import pandas as pd

products = {
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Price": [80000, 1200, 2500],
    "Stock": [5, 20, 15]
}

inventory = pd.DataFrame(products)

print(inventory)