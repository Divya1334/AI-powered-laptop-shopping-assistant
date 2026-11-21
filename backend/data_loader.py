
import pandas as pd

def load_laptops():
    file_path = "data/laptops.csv"

    df = pd.read_csv(file_path)

    df = df.drop_duplicates()
    df.columns = df.columns.str.strip()

    numeric_columns = [
        "price",
        "rating",
        "ram_gb",
        "storage_gb"
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column], errors="coerce"
            )

    return df
