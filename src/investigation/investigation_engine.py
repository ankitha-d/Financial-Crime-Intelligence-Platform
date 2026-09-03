import pandas as pd
import os


def create_investigation_cases(risk_scores, network_features):
    """
    Combine transaction risk signals with account network
    behavior to generate investigation cases.
    """

    df = risk_scores.copy()

    # Merge source account network information
    network = network_features.rename(
        columns={
            "account_id": "source_account_id",
            "incoming_transactions": "source_incoming_transactions",
            "outgoing_transactions": "source_outgoing_transactions",
            "total_connections": "source_total_connections",
            "degree_centrality": "source_degree_centrality"
        }
    )

    df = df.merge(
        network,
        on="source_account_id",
        how="left"
    )

    # Investigation priority
    def determine_priority(row):

        if (
            row["risk_level"] == "HIGH"
            and row["source_total_connections"] >= 10
        ):
            return "CRITICAL"

        elif row["risk_level"] == "HIGH":
            return "HIGH"

        elif row["risk_level"] == "MEDIUM":
            return "MEDIUM"

        else:
            return "LOW"

    df["investigation_priority"] = df.apply(
        determine_priority,
        axis=1
    )

    # Generate investigation reason
    def generate_reason(row):

        reasons = []

        if row["rule_trigger_count"] > 0:
            reasons.append(
                f"{int(row['rule_trigger_count'])} rule trigger(s)"
            )

        if row["is_anomaly"] == 1:
            reasons.append("ML anomaly detected")

        if row["high_value_transaction"] == 1:
            reasons.append("High-value transaction")

        if row["source_total_connections"] >= 10:
            reasons.append("Highly connected account")

        if not reasons:
            reasons.append("Elevated behavioral risk")

        return "; ".join(reasons)

    df["investigation_reason"] = df.apply(
        generate_reason,
        axis=1
    )

    # Investigation case flag
    df["requires_investigation"] = (
        df["investigation_priority"].isin(
            ["CRITICAL", "HIGH"]
        )
    ).astype(int)

    return df


if __name__ == "__main__":

    risk_path = "data/processed/risk_scores.csv"

    network_path = (
        "data/processed/network_features.csv"
    )

    output_path = (
        "data/processed/investigation_cases.csv"
    )

    # Load data
    risk_scores = pd.read_csv(risk_path)

    network_features = pd.read_csv(
        network_path
    )

    print(
        "Creating investigation intelligence..."
    )

    # Create investigation cases
    cases = create_investigation_cases(
        risk_scores,
        network_features
    )

    # Create output directory
    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    # Save cases
    cases.to_csv(
        output_path,
        index=False
    )

    print(
        "\nInvestigation intelligence completed."
    )

    print(
        f"Total transactions analyzed: {len(cases)}"
    )

    print(
        "\nInvestigation priority distribution:"
    )

    print(
        cases[
            "investigation_priority"
        ].value_counts()
    )

    print(
        "\nTransactions requiring investigation:"
    )

    print(
        cases[
            "requires_investigation"
        ].sum()
    )

    print(
        "\nSample investigation cases:"
    )

    print(
        cases[
            cases[
                "requires_investigation"
            ] == 1
        ][
            [
                "transaction_id",
                "source_account_id",
                "amount",
                "risk_score",
                "risk_level",
                "investigation_priority",
                "investigation_reason"
            ]
        ].head(10)
    )