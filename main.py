import subprocess
import sys
import os


def run_module(module_path, module_name):
    """
    Run a platform module and stop the pipeline if it fails.
    """

    print("\n" + "=" * 60)
    print(f"RUNNING: {module_name}")
    print("=" * 60)

    result = subprocess.run(
        [sys.executable, module_path],
        capture_output=False
    )

    if result.returncode != 0:
        print(f"\nERROR: {module_name} failed.")
        sys.exit(1)

    print(f"\nSUCCESS: {module_name} completed.")


if __name__ == "__main__":

    print("\nFINANCIAL CRIME INTELLIGENCE PLATFORM")
    print("=" * 60)

    modules = [

        (
            "src/data_generation/customers_generator.py",
            "Customer Data Generation"
        ),

        (
            "src/data_generation/accounts_generator.py",
            "Account Data Generation"
        ),

        (
            "src/data_generation/transactions_generator.py",
            "Transaction Data Generation"
        ),

        (
            "src/data_quality/data_cleaning.py",
            "Data Quality Processing"
        ),

        (
            "src/feature_engineering/transaction_features.py",
            "Transaction Feature Engineering"
        ),

        (
            "src/feature_engineering/aggregation_features.py",
            "Aggregation Feature Engineering"
        ),

        (
            "src/anomaly_detection/isolation_forest_detector.py",
            "ML Anomaly Detection"
        ),

        (
            "src/rule_engine/rule_engine.py",
            "Rule-Based Detection"
        ),

        (
            "src/risk_scoring/risk_score.py",
            "Risk Scoring"
        ),

        (
            "src/network_analysis/transaction_network.py",
            "Network Analysis"
        ),

        (
            "src/entity_resolution/entity_resolution.py",
            "Entity Resolution"
        ),

        (
            "src/investigation/investigation_engine.py",
            "Investigation Intelligence"
        )

    ]

    for module_path, module_name in modules:

        # Check module exists
        if not os.path.exists(module_path):

            print(
                f"\nWARNING: Module not found: "
                f"{module_path}"
            )

            continue

        run_module(
            module_path,
            module_name
        )

    print("\n" + "=" * 60)
    print("PLATFORM PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)

    print("\nFinal output files are available in:")
    print("data/processed/")