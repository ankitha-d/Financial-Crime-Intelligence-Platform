import pandas as pd


def check_data_quality(df, dataset_name="Dataset"):
    """
    Perform basic data quality checks.
    """

    print(f"\n{'=' * 50}")
    print(f"DATA QUALITY REPORT: {dataset_name}")
    print(f"{'=' * 50}")

    print(f"\nTotal rows: {len(df)}")
    print(f"Total columns: {len(df.columns)}")

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nData types:")
    print(df.dtypes)

    print(f"\n{'=' * 50}\n")


if __name__ == "__main__":

    transactions = pd.read_csv(
        "data/synthetic/transactions.csv"
    )

    check_data_quality(
        transactions,
        "Transactions"
    )