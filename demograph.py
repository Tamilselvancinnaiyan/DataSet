import networkx as nx
import matplotlib.pyplot as plt

# Load a smaller subset of the graph for demonstration purposes
g = nx.read_edgelist('facebook_combined.txt', create_using=nx.Graph(), nodetype=int)
g_subset = g.subgraph(list(g.nodes())[:500])  # Adjust the number of nodes as needed

print("Number of nodes:", g_subset.number_of_nodes())
print("Number of edges:", g_subset.number_of_edges())

# Average degree calculation
avg_degree = sum(dict(g_subset.degree()).values()) / g_subset.number_of_nodes()
print("Average Degree:", avg_degree)

# Spring layout
pos = nx.spring_layout(g_subset, seed=42)

plt.figure(figsize=(10, 8))
nx.draw(g_subset, pos, with_labels=False, node_size=35, edge_color="gray", alpha=0.6)
plt.title("Graph Visualization using Spring Layout")
plt.axis('off')
plt.show()
