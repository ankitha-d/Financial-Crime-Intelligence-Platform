import pandas as pd


def validate_customers(df):
    """
    Validate customer dataset and return data quality results.
    """

    results = {
        "total_rows": len(df),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "invalid_age": int(((df["age"] < 18) | (df["age"] > 100)).sum()),
        "negative_income": int((df["annual_income"] < 0).sum()),
    }

    return results


if __name__ == "__main__":
    customers = pd.read_csv("data/synthetic/customers.csv")

    results = validate_customers(customers)

    print("\nDATA QUALITY REPORT")
    print("-" * 30)

    for key, value in results.items():
        print(f"{key}: {value}")