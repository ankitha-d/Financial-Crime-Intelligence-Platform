import pandas as pd


def create_customer_features(df):
    """
    Create customer-level risk features.
    """

    df = df.copy()

    # Income categories
    df["income_high"] = (
        df["annual_income"] > 1500000
    ).astype(int)

    # Senior customer indicator
    df["is_senior"] = (
        df["age"] >= 60
    ).astype(int)

    # Young customer indicator
    df["is_young"] = (
        df["age"] <= 25
    ).astype(int)

    # Country risk indicator
    df["country_risk"] = (
        df["risk_country_flag"] == 1
    ).astype(int)

    return df


if __name__ == "__main__":

    customers = pd.read_csv(
        "data/synthetic/customers.csv"
    )

    featured_customers = create_customer_features(
        customers
    )

    print("\nCUSTOMER FEATURES CREATED")
    print("-" * 40)

    print(
        featured_customers[
            [
                "customer_id",
                "age",
                "annual_income",
                "income_high",
                "is_senior",
                "is_young",
                "country_risk",
            ]
        ].head()
    )

    featured_customers.to_csv(
        "data/processed/customer_features.csv",
        index=False
    )

    print(
        "\nSaved featured data to "
        "data/processed/customer_features.csv"
    )