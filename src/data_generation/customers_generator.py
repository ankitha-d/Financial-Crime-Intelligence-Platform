import random
import pandas as pd
from pathlib import Path


def generate_customers(n_customers=500, seed=42):
    """
    Generate synthetic customer data for the
    Financial Crime Intelligence Platform.
    """

    random.seed(seed)

    first_names = [
        "Aarav", "Vivaan", "Aditya", "Arjun", "Rohan",
        "Ananya", "Diya", "Kavya", "Sneha", "Priya",
        "Rahul", "Kiran", "Neha", "Vikram", "Meera"
    ]

    last_names = [
        "Sharma", "Patel", "Reddy", "Das", "Kumar",
        "Singh", "Gupta", "Rao", "Verma", "Nair"
    ]

    cities = [
        "Mumbai", "Delhi", "Bengaluru", "Hyderabad",
        "Chennai", "Pune", "Kolkata", "Ahmedabad"
    ]

    occupations = [
        "Software Engineer",
        "Business Owner",
        "Teacher",
        "Doctor",
        "Consultant",
        "Student",
        "Accountant",
        "Manager"
    ]

    customers = []

    for i in range(1, n_customers + 1):

        customer = {
            "customer_id": f"CUST_{i:05d}",
            "first_name": random.choice(first_names),
            "last_name": random.choice(last_names),
            "age": random.randint(18, 75),
            "city": random.choice(cities),
            "occupation": random.choice(occupations),
            "annual_income": random.randint(300000, 3000000),
            "risk_country_flag": random.choices(
                [0, 1],
                weights=[0.95, 0.05]
            )[0]
        }

        customers.append(customer)

    return pd.DataFrame(customers)


if __name__ == "__main__":

    df = generate_customers()

    output_path = Path("data/synthetic")
    output_path.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        output_path / "customers.csv",
        index=False
    )

    print(f"Generated {len(df)} customers successfully.")
    print(df.head())