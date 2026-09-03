import streamlit as st
import pandas as pd
import plotly.express as px
import os


st.set_page_config(
    page_title="Financial Crime Intelligence Platform",
    page_icon="🚨",
    layout="wide"
)


@st.cache_data
def load_data():

    investigation_path = (
        "data/processed/investigation_cases.csv"
    )

    network_path = (
        "data/processed/network_features.csv"
    )

    if not os.path.exists(investigation_path):

        st.error(
            "Investigation data not found. "
            "Please run: python main.py"
        )

        return None, None

    investigations = pd.read_csv(
        investigation_path
    )

    network = pd.read_csv(
        network_path
    )

    return investigations, network


investigations, network = load_data()


if investigations is not None:

    # -------------------------------
    # HEADER
    # -------------------------------

    st.title(
        "🚨 Financial Crime Intelligence Platform"
    )

    st.markdown(
        """
        Detect suspicious financial activity using
        rule-based detection, machine learning,
        risk scoring, and network intelligence.
        """
    )

    st.divider()


    # -------------------------------
    # SIDEBAR FILTERS
    # -------------------------------

    st.sidebar.header("Investigation Filters")

    risk_levels = sorted(
        investigations["risk_level"]
        .dropna()
        .unique()
    )

    selected_risk_levels = st.sidebar.multiselect(
        "Risk Level",
        options=risk_levels,
        default=risk_levels
    )

    priorities = sorted(
        investigations["investigation_priority"]
        .dropna()
        .unique()
    )

    selected_priorities = st.sidebar.multiselect(
        "Investigation Priority",
        options=priorities,
        default=priorities
    )

    countries = sorted(
        investigations["country"]
        .dropna()
        .unique()
    )

    selected_countries = st.sidebar.multiselect(
        "Country",
        options=countries,
        default=countries
    )


    filtered_df = investigations[
        investigations["risk_level"]
        .isin(selected_risk_levels)
        &
        investigations["investigation_priority"]
        .isin(selected_priorities)
        &
        investigations["country"]
        .isin(selected_countries)
    ]


    # -------------------------------
    # KPI METRICS
    # -------------------------------

    total_transactions = len(filtered_df)

    high_risk = len(
        filtered_df[
            filtered_df["risk_level"] == "HIGH"
        ]
    )

    anomalies = int(
        filtered_df["is_anomaly"].sum()
    )

    investigations_required = int(
        filtered_df[
            "requires_investigation"
        ].sum()
    )


    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Transactions",
        f"{total_transactions:,}"
    )

    col2.metric(
        "High Risk",
        f"{high_risk:,}"
    )

    col3.metric(
        "ML Anomalies",
        f"{anomalies:,}"
    )

    col4.metric(
        "Investigation Cases",
        f"{investigations_required:,}"
    )


    st.divider()


    # -------------------------------
    # CHARTS
    # -------------------------------

    col1, col2 = st.columns(2)

    with col1:

        risk_chart = px.histogram(
            filtered_df,
            x="risk_level",
            title="Risk Level Distribution"
        )

        st.plotly_chart(
            risk_chart,
            use_container_width=True
        )


    with col2:

        priority_chart = px.histogram(
            filtered_df,
            x="investigation_priority",
            title="Investigation Priority Distribution"
        )

        st.plotly_chart(
            priority_chart,
            use_container_width=True
        )


    # -------------------------------
    # RISK SCORE DISTRIBUTION
    # -------------------------------

    risk_score_chart = px.histogram(
        filtered_df,
        x="risk_score",
        nbins=30,
        title="Risk Score Distribution"
    )

    st.plotly_chart(
        risk_score_chart,
        use_container_width=True
    )


    # -------------------------------
    # TOP INVESTIGATION CASES
    # -------------------------------

    st.subheader(
        "🔴 Top Investigation Cases"
    )

    top_cases = filtered_df[
        filtered_df[
            "requires_investigation"
        ] == 1
    ].sort_values(
        "risk_score",
        ascending=False
    )

    display_columns = [

        "transaction_id",
        "source_account_id",
        "destination_account_id",
        "amount",
        "country",
        "risk_score",
        "risk_level",
        "investigation_priority",
        "investigation_reason"

    ]

    st.dataframe(
        top_cases[
            display_columns
        ],
        use_container_width=True,
        height=400
    )


    # -------------------------------
    # NETWORK ANALYSIS
    # -------------------------------

    st.divider()

    st.subheader(
        "🕸️ Account Network Intelligence"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total Accounts",
            f"{len(network):,}"
        )


    with col2:

        avg_connections = (
            network[
                "total_connections"
            ].mean()
        )

        st.metric(
            "Average Connections",
            f"{avg_connections:.2f}"
        )


    top_network = network.sort_values(
        "degree_centrality",
        ascending=False
    ).head(20)


    network_chart = px.bar(
        top_network,
        x="account_id",
        y="degree_centrality",
        title="Top Connected Accounts"
    )

    st.plotly_chart(
        network_chart,
        use_container_width=True
    )


    # -------------------------------
    # RAW DATA
    # -------------------------------

    st.divider()

    st.subheader(
        "📄 Filtered Investigation Data"
    )

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=500
    )


else:

    st.warning(
        "Run the pipeline first to generate data."
    )