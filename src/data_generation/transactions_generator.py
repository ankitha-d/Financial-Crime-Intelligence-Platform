import random
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd


def generate_transactions(n_transactions=10000, n_accounts=1000, seed=42):
    """
    Generate synthetic banking transactions.
    Includes a small percentage of suspicious transactions.
    """

    random.seed(seed)
    np.random.seed(seed)

    transaction_types = [
        "TRANSFER",
        "PAYMENT",
        "WITHDRAWAL",
        "DEPOSIT"
    ]

    channels = [
        "ONLINE",
        "ATM",
        "MOBILE",
        "BRANCH"
    ]

    countries = [
        "India",
        "USA",
        "UK",
        "Singapore",
        "UAE",
        "Hong Kong"
    ]

    transactions = []

    start_date = datetime.now() - timedelta(days=180)

    for i in range(1, n_transactions + 1):

        is_suspicious = random.choices(
            [0, 1],
            weights=[0.95, 0.05]
        )[0]

        transaction_date = (
            start_date +
            timedelta(
                seconds=random.randint(0, 180 * 24 * 60 * 60)
            )
        )

        amount = round(
            np.random.lognormal(
                mean=9,
                sigma=1.2
            ),
            2
        )

        if is_suspicious:

            # Generate unusually large transaction amounts
            amount *= random.uniform(5, 20)

        transaction = {
            "transaction_id": f"TXN_{i:07d}",
            "source_account_id": f"ACC_{random.randint(1, n_accounts):06d}",
            "destination_account_id": f"ACC_{random.randint(1, n_accounts):06d}",
            "transaction_timestamp": transaction_date,
            "transaction_type": random.choice(transaction_types),
            "amount": round(amount, 2),
            "channel": random.choice(channels),
            "country": random.choice(countries),
            "is_suspicious": is_suspicious
        }

        transactions.append(transaction)

    return pd.DataFrame(transactions)


if __name__ == "__main__":

    df = generate_transactions()

    output_path = Path("data/synthetic")
    output_path.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        output_path / "transactions.csv",
        index=False
    )

    print(f"Generated {len(df)} transactions successfully.")
    print(f"Suspicious transactions: {df['is_suspicious'].sum()}")
    print(df.head())