import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Financial Crime Intelligence Platform",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Financial Crime Intelligence Platform")
st.markdown(
    "AI-powered transaction monitoring, anomaly detection, "
    "rule-based detection, and risk scoring."
)

DATA_PATH ="data/processed/risk_scores.csv"

if not os.path.exists(DATA_PATH):
    st.error(
        "Risk scored data not found. Please run the risk scoring pipeline first."
    )
    st.stop()

df = pd.read_csv(DATA_PATH)

# Metrics
total_transactions = len(df)

if "is_anomaly" in df.columns:
    anomalies = int(df["is_anomaly"].sum())
else:
    anomalies = 0

if "risk_level" in df.columns:
    high_risk = len(df[df["risk_level"] == "HIGH"])
else:
    high_risk = 0

avg_amount = df["amount"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Transactions", f"{total_transactions:,}")
col2.metric("Anomalies Detected", f"{anomalies:,}")
col3.metric("High Risk Transactions", f"{high_risk:,}")
col4.metric("Average Transaction", f"₹{avg_amount:,.0f}")

st.divider()

st.subheader("📊 Risk Distribution")

if "risk_level" in df.columns:
    risk_counts = df["risk_level"].value_counts()
    st.bar_chart(risk_counts)

st.divider()

st.subheader("🚨 High Risk Transactions")

if "risk_level" in df.columns:
    high_risk_df = df[df["risk_level"] == "HIGH"]

    if len(high_risk_df) > 0:
        display_columns = [
            col for col in [
                "transaction_id",
                "source_account_id",
                "destination_account_id",
                "amount",
                "country",
                "transaction_type",
                "anomaly_score",
                "rule_trigger_count",
                "risk_score",
                "risk_level"
            ]
            if col in high_risk_df.columns
        ]

        st.dataframe(
            high_risk_df[display_columns],
            use_container_width=True
        )
    else:
        st.info("No high-risk transactions found.")

st.divider()

st.subheader("🔎 Explore Transactions")

st.dataframe(df, use_container_width=True)