import pandas as pd
import networkx as nx
import os


def build_transaction_network(df):
    """
    Build a directed graph where:
    - Nodes = bank accounts
    - Edges = transactions between accounts
    """

    G = nx.DiGraph()

    for _, row in df.iterrows():

        source = row["source_account_id"]
        destination = row["destination_account_id"]

        G.add_edge(
            source,
            destination,
            transaction_id=row["transaction_id"],
            amount=row["amount"],
            risk_level=row.get("risk_level", "UNKNOWN"),
            risk_score=row.get("risk_score", 0)
        )

    return G


def calculate_network_features(G):

    # Convert to undirected graph for some centrality calculations
    undirected_G = G.to_undirected()

    degree_centrality = nx.degree_centrality(undirected_G)

    # Create account-level feature records
    records = []

    for node in G.nodes():

        incoming_transactions = G.in_degree(node)
        outgoing_transactions = G.out_degree(node)

        total_connections = incoming_transactions + outgoing_transactions

        records.append({
            "account_id": node,
            "incoming_transactions": incoming_transactions,
            "outgoing_transactions": outgoing_transactions,
            "total_connections": total_connections,
            "degree_centrality": degree_centrality.get(node, 0)
        })

    return pd.DataFrame(records)


if __name__ == "__main__":

    input_path = "data/processed/risk_scores.csv"
    output_path = "data/processed/network_features.csv"

    # Load transactions with risk scores
    transactions = pd.read_csv(input_path)

    print("Building transaction network...")

    G = build_transaction_network(transactions)

    print(f"Total accounts (nodes): {G.number_of_nodes()}")
    print(f"Total transaction relationships (edges): {G.number_of_edges()}")

    print("\nCalculating network features...")

    network_features = calculate_network_features(G)

    # Create output directory
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save results
    network_features.to_csv(output_path, index=False)

    print("\nNetwork analysis completed successfully.")

    print("\nSample network features:")
    print(network_features.head())