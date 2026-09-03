import pandas as pd
import os


def find_duplicate_customers(customers):
    """
    Identify potentially duplicate customers based on
    matching names and demographic attributes.
    """

    customers = customers.copy()

    customers["full_name"] = (
        customers["first_name"].str.lower().str.strip()
        + " "
        + customers["last_name"].str.lower().str.strip()
    )

    duplicate_groups = customers.groupby(
        ["full_name", "city"]
    ).filter(lambda x: len(x) > 1)

    return duplicate_groups


def create_entity_features(customers):
    """
    Create entity-resolution features.
    """

    customers = customers.copy()

    customers["full_name"] = (
        customers["first_name"].str.lower().str.strip()
        + " "
        + customers["last_name"].str.lower().str.strip()
    )

    name_counts = customers.groupby("full_name")[
        "customer_id"
    ].transform("count")

    customers["same_name_count"] = name_counts

    customers["potential_duplicate"] = (
        customers["same_name_count"] > 1
    ).astype(int)

    return customers


if __name__ == "__main__":

    input_path = "data/synthetic/customers.csv"

    output_path = (
        "data/processed/entity_resolution_results.csv"
    )

    # Load customer data
    customers = pd.read_csv(input_path)

    print(
        f"Total customers: {len(customers)}"
    )

    # Create entity features
    entity_results = create_entity_features(customers)

    # Find duplicate candidates
    duplicates = find_duplicate_customers(
        customers
    )

    print(
        f"Potential duplicate records: "
        f"{len(duplicates)}"
    )

    # Create output directory
    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    # Save entity resolution results
    entity_results.to_csv(
        output_path,
        index=False
    )

    print(
        "\nEntity resolution completed successfully."
    )

    print(
        "\nSample results:"
    )

    print(
        entity_results[
            [
                "customer_id",
                "full_name",
                "city",
                "same_name_count",
                "potential_duplicate"
            ]
        ].head(10)
    )