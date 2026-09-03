import pandas as pd


def apply_suspicious_rules(df):
    """
    Apply rule-based financial crime detection rules.
    """

    df = df.copy()

    # Rule 1: High-value transaction
    df["rule_high_value"] = (
        df["amount"] >= 100000
    ).astype(int)

    # Rule 2: Unusual transaction hour
    df["rule_unusual_hour"] = (
        (df["transaction_hour"] < 6)
        | (df["transaction_hour"] >= 23)
    ).astype(int)

    # Rule 3: Suspicious country
    suspicious_countries = [
        "Hong Kong",
        "Russia",
        "Nigeria"
    ]

    df["rule_suspicious_country"] = (
        df["country"].isin(suspicious_countries)
    ).astype(int)

    # Rule 4: Known suspicious transaction label
    df["rule_known_suspicious"] = (
        df["is_suspicious"] == 1
    ).astype(int)

    # Total triggered rules
    rule_columns = [
        "rule_high_value",
        "rule_unusual_hour",
        "rule_suspicious_country",
        "rule_known_suspicious",
    ]

    df["rule_score"] = df[rule_columns].sum(axis=1)

    return df


if __name__ == "__main__":

    transactions = pd.read_csv(
        "data/processed/transactions_features.csv"
    )

    results = apply_suspicious_rules(transactions)

    print("\nRULE ENGINE RESULTS")
    print("-" * 40)

    print(
        results[
            [
                "transaction_id",
                "amount",
                "country",
                "rule_score",
            ]
        ].head(10)
    )

    print("\nRule score distribution:")

    print(
        results["rule_score"].value_counts()
        .sort_index()
    )

    results.to_csv(
        "data/processed/rule_results.csv",
        index=False
    )

    print(
        "\nSaved results to "
        "data/processed/rule_results.csv"
    )