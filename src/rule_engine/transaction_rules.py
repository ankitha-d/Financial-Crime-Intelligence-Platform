import pandas as pd


def apply_transaction_rules(df):
    """
    Apply rule-based financial crime detection rules.
    """

    df = df.copy()

    # Rule 1: Very high transaction amount
    df["rule_high_amount"] = (
        df["amount"] > 100000
    ).astype(int)

    # Rule 2: Transaction involving higher-risk countries
    high_risk_countries = [
        "Hong Kong",
        "UAE"
    ]

    df["rule_high_risk_country"] = (
        df["country"].isin(high_risk_countries)
    ).astype(int)

    # Rule 3: Unusual transaction hours
    df["rule_unusual_hour"] = (
        (df["transaction_hour"] < 5) |
        (df["transaction_hour"] > 23)
    ).astype(int)

    # Total number of triggered rules
    rule_columns = [
        "rule_high_amount",
        "rule_high_risk_country",
        "rule_unusual_hour"
    ]

    df["rule_trigger_count"] = (
        df[rule_columns].sum(axis=1)
    )

    return df


if __name__ == "__main__":

    transactions = pd.read_csv(
        "data/processed/anomaly_results.csv"
    )

    results = apply_transaction_rules(transactions)

    results.to_csv(
        "data/processed/rule_results.csv",
        index=False
    )

    print("Rule engine completed successfully.")

    print("\nRule trigger summary:")
    print(
        results[
            [
                "rule_high_amount",
                "rule_high_risk_country",
                "rule_unusual_hour"
            ]
        ].sum()
    )

    print("\nTransactions triggering rules:")
    print(
        results[
            results["rule_trigger_count"] > 0
        ][
            [
                "transaction_id",
                "amount",
                "country",
                "transaction_hour",
                "rule_trigger_count"
            ]
        ].head()
    )