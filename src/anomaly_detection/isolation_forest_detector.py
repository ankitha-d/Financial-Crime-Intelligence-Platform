import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(df, contamination=0.05):
    """
    Detect anomalous transactions using Isolation Forest.
    """

    df = df.copy()

    feature_columns = [
        "amount",
        "transaction_hour",
        "transaction_day_of_week",
        "high_value_transaction",
        "log_amount"
    ]

    X = df[feature_columns]

    model = IsolationForest(
        n_estimators=100,
        contamination=contamination,
        random_state=42
    )

    model.fit(X)

    # Isolation Forest returns -1 for anomalies and 1 for normal records
    predictions = model.predict(X)

    df["anomaly_prediction"] = predictions

    # Convert to easier-to-read binary flag
    df["is_anomaly"] = (
        df["anomaly_prediction"] == -1
    ).astype(int)

    # Anomaly score: lower scores generally indicate more anomalous records
    df["anomaly_score"] = model.decision_function(X)

    return df, model


if __name__ == "__main__":

    transactions = pd.read_csv(
        "data/processed/transactions_features.csv"
    )

    results, model = detect_anomalies(transactions)

    results.to_csv(
        "data/processed/anomaly_results.csv",
        index=False
    )

    print("Anomaly detection completed successfully.")
    print(f"Total transactions: {len(results)}")
    print(f"Anomalies detected: {results['is_anomaly'].sum()}")

    print("\nSample anomalies:")
    print(
        results[
            results["is_anomaly"] == 1
        ][
            [
                "transaction_id",
                "amount",
                "transaction_hour",
                "anomaly_score"
            ]
        ].head()
    )