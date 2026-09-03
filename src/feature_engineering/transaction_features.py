import pandas as pd


def create_transaction_features(df):
    """
    Create useful features for financial crime detection.
    """

    df = df.copy()

    # Ensure timestamp is a datetime
    df["transaction_timestamp"] = pd.to_datetime(
        df["transaction_timestamp"]
    )

    # Transaction amount features
    df["high_value_transaction"] = (
        df["amount"] > 100000
    ).astype(int)

    # Keep a descriptive alias for readability
    df["is_high_value"] = df["high_value_transaction"]

    # Log transformation for transaction amount
    df["log_amount"] = (
        df["amount"] + 1
    ).apply(lambda x: __import__("math").log(x))

    # Time-based features
    df["transaction_hour"] = (
        df["transaction_timestamp"].dt.hour
    )

    df["transaction_day_of_week"] = (
        df["transaction_timestamp"].dt.dayofweek
    )

    # Flag unusual transaction hours
    df["is_unusual_hour"] = (
        (df["transaction_hour"] < 6)
        | (df["transaction_hour"] > 22)
    ).astype(int)

    return df


if __name__ == "__main__":

    transactions = pd.read_csv(
        "data/synthetic/transactions.csv"
    )

    featured_transactions = create_transaction_features(
        transactions
    )

    print("\nTRANSACTION FEATURES CREATED")
    print("-" * 40)

    print(
        featured_transactions[
            [
                "transaction_id",
                "amount",
                "high_value_transaction",
                "transaction_hour",
                "transaction_day_of_week",
                "log_amount",
                "is_unusual_hour",
            ]
        ].head()
    )

    featured_transactions.to_csv(
        "data/processed/transactions_features.csv",
        index=False
    )

    print(
        "\nSaved featured data to "
        "data/processed/transactions_features.csv"
    )