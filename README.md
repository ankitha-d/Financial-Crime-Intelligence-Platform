# 🔍 Financial Crime Intelligence Platform

An end-to-end Financial Crime Intelligence Platform designed to identify suspicious transactions using anomaly detection, rule-based monitoring, risk scoring, network analysis, and entity resolution.

## 🚀 Live Demo

🔗 Streamlit Application: https://financial-crime-intelligence-platform-8phklg6eodkk6odb9cc6r6.streamlit.app/

## 📌 Project Overview

Financial institutions process millions of transactions every day, making manual detection of suspicious activity difficult.

This platform simulates a financial transaction monitoring system that combines multiple analytical techniques to identify potentially suspicious transactions and prioritize them based on risk.

The platform includes:

* Synthetic customer and transaction data generation
* Data quality checks
* Feature engineering
* Transaction aggregation
* Isolation Forest anomaly detection
* Rule-based suspicious activity detection
* Risk scoring
* Entity resolution
* Network analysis
* Investigation case generation
* Interactive Streamlit dashboard

## 🏗️ Project Architecture

```text
Raw Data
   │
   ▼
Data Quality Checks
   │
   ▼
Feature Engineering
   │
   ├──────────────► Aggregation Features
   │
   ▼
Anomaly Detection
   │
   ▼
Rule Engine
   │
   ▼
Risk Scoring
   │
   ├──────────────► Entity Resolution
   │
   ├──────────────► Network Analysis
   │
   ▼
Investigation Cases
   │
   ▼
Streamlit Dashboard
```

## 🧠 Key Features

### 🔎 Anomaly Detection

Uses the Isolation Forest algorithm to identify unusual transactions based on engineered transaction features.

### 📜 Rule Engine

Detects suspicious patterns using business rules such as:

* High-value transactions
* Transactions involving high-risk countries
* Transactions occurring during unusual hours
* Multiple rule triggers

### ⚠️ Risk Scoring

Combines signals from:

* Rule-based detection
* Anomaly detection
* Transaction characteristics

Transactions are assigned a risk score and categorized by risk level.

### 🕸️ Network Analysis

Analyzes relationships between accounts to identify potentially suspicious transaction networks.

### 👤 Entity Resolution

Identifies potential duplicate or similar customer entities to support investigation workflows.

### 📁 Investigation Cases

Generates investigation-ready cases for transactions requiring further review.

## 📊 Technology Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* NetworkX
* Jupyter Notebook

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

Activate the environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Dashboard

```bash
streamlit run dashboard/app.py
```

## 🌐 Deployment

The application is deployed using Streamlit Community Cloud.

Live Application:

https://financial-crime-intelligence-platform-8phklg6eodkk6odb9cc6r6.streamlit.app/

## 🎯 Skills Demonstrated

* Data Engineering
* Feature Engineering
* Machine Learning
* Anomaly Detection
* Financial Risk Analytics
* Rule-Based Systems
* Network Analysis
* Entity Resolution
* Data Visualization
* Streamlit Deployment

## 👩‍💻 Author

**Ankitha D**

GitHub: https://github.com/ankitha-d
