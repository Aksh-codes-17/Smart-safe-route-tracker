import networkx as nx
import json

# Load dataset
with open("data.json") as f:
    data = json.load(f)

G = nx.Graph()

# Build graph
for edge in data["edges"]:
    G.add_edge(
        edge["from"],
        edge["to"],
        distance=edge["distance"],
        crime=edge["crime"],
        lighting=edge["lighting"]
    )

def calculate_weight(u, v, d):
    # Combine safety factors
    return d["distance"] + (d["crime"] * 2) - d["lighting"]

def get_safe_route(source, destination):
    path = nx.shortest_path(
        G,
        source=source,
        target=destination,
        weight=calculate_weight
    )
    return path
