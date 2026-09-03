import pandas as pd


def validate_transactions(df):
    """
    Validate transaction dataset.
    """

    results = {
        "total_transactions": len(df),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_transactions": int(df.duplicated().sum()),
        "negative_amounts": int((df["amount"] < 0).sum()),
        "zero_amounts": int((df["amount"] == 0).sum()),
    }

    return results


if __name__ == "__main__":
    transactions = pd.read_csv("data/synthetic/transactions.csv")

    results = validate_transactions(transactions)

    print("\nTRANSACTION DATA QUALITY REPORT")
    print("-" * 40)

    for key, value in results.items():
        print(f"{key}: {value}")