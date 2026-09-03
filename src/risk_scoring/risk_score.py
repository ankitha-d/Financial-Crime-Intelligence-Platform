import pandas as pd
import os


def calculate_risk_score(df):

    # Rule-based risk points
    df["rule_risk_points"] = df["rule_trigger_count"] * 20

    # Anomaly risk points
    df["anomaly_risk_points"] = df["is_anomaly"] * 40

    # High-value transaction risk
    df["high_value_risk_points"] = df["high_value_transaction"] * 15

    # Total risk score
    df["risk_score"] = (
        df["rule_risk_points"]
        + df["anomaly_risk_points"]
        + df["high_value_risk_points"]
    )

    # Cap score at 100
    df["risk_score"] = df["risk_score"].clip(upper=100)

    # Risk classification
    def classify_risk(score):

        if score >= 70:
            return "HIGH"

        elif score >= 40:
            return "MEDIUM"

        else:
            return "LOW"

    df["risk_level"] = df["risk_score"].apply(classify_risk)

    return df


if __name__ == "__main__":

    input_path = "data/processed/rule_results.csv"
    output_path = "data/processed/risk_scores.csv"

    # Load rule engine results
    results = pd.read_csv(input_path)

    # Calculate risk
    results = calculate_risk_score(results)

    # Create output directory if needed
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save results
    results.to_csv(output_path, index=False)

    print("Risk scoring completed successfully.")

    print(f"\nTotal transactions: {len(results)}")

    print("\nRisk level distribution:")
    print(results["risk_level"].value_counts())

    print("\nSample high-risk transactions:")

    high_risk = results[
        results["risk_level"] == "HIGH"
    ][
        [
            "transaction_id",
            "amount",
            "rule_trigger_count",
            "is_anomaly",
            "risk_score",
            "risk_level"
        ]
    ]

    print(high_risk.head())