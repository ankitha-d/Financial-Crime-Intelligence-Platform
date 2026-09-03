# 🔍 Financial Crime Intelligence Platform

An end-to-end **Financial Crime Intelligence Platform** that simulates transaction monitoring and investigation workflows using anomaly detection, rule-based monitoring, risk scoring, network analysis, entity resolution, and investigation prioritization.

## 🚀 Live Demo

🔗 **Streamlit Application:**
https://financial-crime-intelligence-platform-8phklg6eodkk6odb9cc6r6.streamlit.app/

## 📌 Project Overview

Financial institutions process large volumes of transactions, making manual identification and prioritization of potentially suspicious activity difficult.

This project simulates a financial crime analytics workflow using synthetic transaction data. Multiple analytical signals are combined to identify unusual activity, assign risk levels, and prioritize transactions for further investigation.

> **Disclaimer:** This project uses synthetic data and simulated detection rules for educational and portfolio purposes. It is not intended for production AML compliance or regulatory decision-making.

### Platform Workflow

```text
Synthetic Data Generation
        │
        ▼
Data Quality & Validation
        │
        ▼
Feature Engineering
        │
        ├──────────────► Aggregation Features
        │
        ▼
ML Anomaly Detection
        │
        ▼
Rule-Based Detection
        │
        ▼
Risk Scoring
        │
        ├──────────────► Entity Resolution
        │
        ├──────────────► Network Analysis
        │
        ▼
Investigation Intelligence
        │
        ▼
Streamlit Dashboard
```

## 🧠 Key Features

### 🔎 Anomaly Detection

Uses the **Isolation Forest** algorithm to identify unusual transactions based on engineered transaction characteristics including:

* Transaction amount
* Log-transformed transaction amount
* Transaction hour
* Day of week
* High-value transaction indicator

The current configuration uses a **5% Isolation Forest contamination setting**.

### 📜 Rule-Based Monitoring

Applies configurable transaction-monitoring rules based on:

* High-value transactions
* Geographic-risk indicators
* Unusual transaction hours
* Multiple simultaneous rule triggers

### ⚠️ Risk Scoring

Combines multiple analytical signals into a transaction-level risk score.

The current scoring model considers:

* Rule-trigger count
* ML anomaly detection
* High-value transaction indicators

Transactions are categorized into **LOW, MEDIUM, and HIGH** risk levels.

### 🕸️ Network Analysis

Builds a transaction network connecting source and destination accounts.

Network features include:

* Incoming transaction relationships
* Outgoing transaction relationships
* Total connections
* Degree centrality

These features support identification of accounts with potentially unusual transaction connectivity.

### 👤 Entity Resolution

Normalizes customer names and identifies potential duplicate entities using matching characteristics such as:

* Customer name
* City
* Name frequency

Potential duplicate records are surfaced for further investigation rather than treated as confirmed matches.

### 📁 Investigation Intelligence

Combines transaction risk and network information to prioritize transactions for investigation.

Investigation records include:

* Risk level
* Investigation priority
* Investigation reason
* Network characteristics
* Detection signals

## 📊 Results

The current synthetic dataset contains **10,000 transactions**.

| Metric                               | Result |
| ------------------------------------ | -----: |
| Transactions analyzed                | 10,000 |
| ML anomalies detected                |    500 |
| High-value rule triggers             |    405 |
| Geographic-risk rule triggers        |  3,305 |
| Unusual-hour rule triggers           |  1,998 |
| Transactions requiring investigation |    421 |
| Customers analyzed                   |    500 |
| Accounts represented in network      |  1,000 |

The Isolation Forest detected **500 anomalies**, representing **5% of the transaction dataset under the current configured contamination level**.

## 🛠️ Technology Stack

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **NetworkX**
* **Plotly**
* **Streamlit**
* **Git / GitHub**

## 📂 Project Structure

```text
Financial-Crime-Intelligence-Platform/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── synthetic/
│   └── processed/
│
├── src/
│   ├── anomaly_detection/
│   ├── data_generation/
│   ├── data_quality/
│   ├── entity_resolution/
│   ├── feature_engineering/
│   ├── investigation/
│   ├── network_analysis/
│   ├── risk_scoring/
│   └── rule_engine/
│
├── main.py
├── config.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ankitha-d/Financial-Crime-Intelligence-Platform.git
```

Navigate to the project:

```bash
cd Financial-Crime-Intelligence-Platform
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Complete Pipeline

Run the end-to-end analytical pipeline:

```bash
python main.py
```

The pipeline executes:

1. Customer data generation
2. Account data generation
3. Transaction data generation
4. Transaction feature engineering
5. Aggregation feature engineering
6. ML anomaly detection
7. Rule-based detection
8. Risk scoring
9. Network analysis
10. Entity resolution
11. Investigation intelligence

Generated analytical outputs are stored in:

```text
data/processed/
```

## 📊 Run the Dashboard

Launch the interactive Streamlit dashboard:

```bash
streamlit run dashboard/app.py
```

The dashboard provides an interactive view of transaction risk and investigation results.

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

### Live Application

https://financial-crime-intelligence-platform-8phklg6eodkk6odb9cc6r7.streamlit.app/

## 🎯 Skills Demonstrated

* Data Processing & Validation
* Feature Engineering
* Machine Learning
* Anomaly Detection
* Financial Risk Analytics
* Rule-Based Detection
* Risk Scoring
* Network Analysis
* Entity Resolution
* Investigation Prioritization
* Data Visualization
* Streamlit Development
* Cloud Deployment
* Git / GitHub

## 🔮 Future Improvements

Potential future extensions include:

* Persistent database integration
* SQL-based analytical workflows
* More advanced behavioral features
* Graph-based suspicious activity detection
* Explainable risk scoring
* Automated investigation reporting
* Model evaluation against labeled synthetic scenarios
* More sophisticated entity matching

## 👩‍💻 Author

**Ankitha D**

GitHub:
https://github.com/ankitha-d
