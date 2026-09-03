import pandas as pd


def create_account_transaction_features(transactions):
    """
    Create aggregated transaction features for each source account.
    """

    account_features = (
        transactions
        .groupby("source_account_id")
        .agg(
            transaction_count=("transaction_id", "count"),
            total_transaction_amount=("amount", "sum"),
            average_transaction_amount=("amount", "mean"),
            max_transaction_amount=("amount", "max"),
            min_transaction_amount=("amount", "min"),
            transaction_amount_std=("amount", "std"),
            suspicious_transaction_count=("is_suspicious", "sum"),
        )
        .reset_index()
    )

    account_features["transaction_amount_std"] = (
        account_features["transaction_amount_std"].fillna(0)
    )

    return account_features


if __name__ == "__main__":

    transactions = pd.read_csv(
        "data/synthetic/transactions.csv"
    )

    account_features = create_account_transaction_features(
        transactions
    )

    print("\nACCOUNT TRANSACTION AGGREGATION FEATURES")
    print("-" * 55)

    print(account_features.head())

    account_features.to_csv(
        "data/processed/account_transaction_features.csv",
        index=False
    )

    print(
        "\nSaved to "
        "data/processed/account_transaction_features.csv"
    )