import networkx as nx
import matplotlib.pyplot as plt
import threading

# Load the full graph
g = nx.read_edgelist('facebook_combined.txt', create_using=nx.Graph(), nodetype=int)

# Sample a subset of nodes
nodes_subset = list(g.nodes())[:100]
g_subset = g.subgraph(nodes_subset)

print("Number of nodes in the subset:", g_subset.number_of_nodes())
print("Number of edges in the subset:", g_subset.number_of_edges())

# Average degree calculation
avg_degree = sum(dict(g_subset.degree()).values()) / g_subset.number_of_nodes()
print("Average Degree:", avg_degree)

# Threaded Kamada-Kawai layout
def kamada_kawai_layout_threaded(graph):
    layout_thread = threading.Thread(target=nx.kamada_kawai_layout, args=(graph,))
    layout_thread.start()
    layout_thread.join(timeout=60)  # Set the timeout value (in seconds)

kamada_kawai_layout_threaded(g_subset)

# Display the graph
plt.figure(figsize=(10, 8))
nx.draw(g_subset, with_labels=True, node_size=35, edge_color="gray", alpha=0.6)
plt.title("Graph Visualization using Kamada-Kawai Layout (Subset)")
plt.axis('off')
plt.show()
