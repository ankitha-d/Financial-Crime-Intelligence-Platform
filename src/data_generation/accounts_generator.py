import random
import pandas as pd
from pathlib import Path


def generate_accounts(n_customers=500, seed=42):
    """
    Generate synthetic bank account data.
    Each customer can have 1 to 3 accounts.
    """

    random.seed(seed)

    account_types = [
        "Savings",
        "Current",
        "Salary",
        "Business"
    ]

    accounts = []
    account_number = 1

    for customer_num in range(1, n_customers + 1):

        customer_id = f"CUST_{customer_num:05d}"

        num_accounts = random.randint(1, 3)

        for _ in range(num_accounts):

            account = {
                "account_id": f"ACC_{account_number:06d}",
                "customer_id": customer_id,
                "account_type": random.choice(account_types),
                "balance": random.randint(1000, 5000000),
                "account_status": random.choices(
                    ["Active", "Dormant", "Closed"],
                    weights=[0.85, 0.10, 0.05]
                )[0]
            }

            accounts.append(account)
            account_number += 1

    return pd.DataFrame(accounts)


if __name__ == "__main__":

    df = generate_accounts()

    output_path = Path("data/synthetic")
    output_path.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        output_path / "accounts.csv",
        index=False
    )

    print(f"Generated {len(df)} accounts successfully.")
    print(df.head())