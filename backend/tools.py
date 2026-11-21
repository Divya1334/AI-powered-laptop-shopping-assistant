
from backend.data_loader import load_laptops

df = load_laptops()

def search_laptops(
    max_price=None,
    min_ram=None,
    min_storage=None,
    brand=None
):
    result = df.copy()

    if max_price is not None:
        result = result[result["price"] <= max_price]

    if min_ram is not None:
        result = result[result["ram_gb"] >= min_ram]

    if min_storage is not None:
        result = result[result["storage_gb"] >= min_storage]

    if brand is not None:
        result = result[
            result["brand"].str.contains(
                brand, case=False, na=False
            )
        ]

    return result


def compare_laptops(brand1, brand2):
    result = df[
        df["brand"].str.contains(
            brand1, case=False, na=False
        ) |
        df["brand"].str.contains(
            brand2, case=False, na=False
        )
    ]

    columns = [
        "brand",
        "model",
        "price",
        "rating",
        "cpu_brand",
        "ram_gb",
        "storage_gb",
        "gpu_brand"
    ]

    available = [
        col for col in columns
        if col in result.columns
    ]

    return result[available].head(10)



def recommend_laptops(
    max_price=None,
    min_ram=None,
    min_storage=None,
    top_n=3
):
    result = search_laptops(
        max_price=max_price,
        min_ram=min_ram,
        min_storage=min_storage
    )

    if result.empty:
        return result

    result = result.sort_values(
        by=["rating", "price"],
        ascending=[False, True],
        na_position="last"
    )

    return result.head(top_n)
