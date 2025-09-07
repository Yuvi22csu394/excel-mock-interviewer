# utils/dataset_generator.py
import pandas as pd
import random

def example_dataset_by_seed(seed: int = None):
    """
    Return a professional example dataset (pandas DataFrame).
    You can expand this to create datasets per question type.
    """
    if seed is not None:
        random.seed(seed)
    products = [
        "Apple", "Banana", "Avocado", "Blueberry", "Almond", "Blackberry", "Coconut", "Date", "Elderberry"
    ]
    regions = ["North", "South", "East", "West"]
    rows = []
    for i in range(12):
        rows.append({
            "ProductID": 100 + i,
            "ProductName": random.choice(products),
            "Sales": random.randint(50, 400),
            "Region": random.choice(regions),
            "Month": random.choice(["Jan", "Feb", "Mar", "Apr"])
        })
    df = pd.DataFrame(rows)
    return df
