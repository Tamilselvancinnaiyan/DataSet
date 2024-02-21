import networkx as nx
import matplotlib.pyplot as plt
import threading

# Load the full graph
g = nx.read_edgelist('facebook_combined.txt', create_using=nx.Graph(), nodetype=int)

# Sample a subset of nodes
nodes_subset = list(g.nodes())[:1000]
g_subset = g.subgraph(nodes_subset)

print("Number of nodes in the subset:", g_subset.number_of_nodes())
print("Number of edges in the subset:", g_subset.number_of_edges())

# 1. Number of Triangles
triangles = sum(nx.triangles(g_subset).values()) // 3
print("Number of Triangles:", triangles)

# 2. Diameter
try:
    diameter = nx.diameter(g_subset)
    print("Diameter:", diameter)
except nx.NetworkXError:
    print("Diameter: Infinite")

# 3. Number of components
num_components = nx.number_connected_components(g_subset)
print("Number of Components:", num_components)

# 4. Size of largest connected component
largest_cc = max(nx.connected_components(g_subset), key=len)
size_largest_cc = len(largest_cc)
print("Size of Largest Connected Component:", size_largest_cc)

# 5. Clustering Coefficient
avg_clustering_coefficient = nx.average_clustering(g_subset)
print("Clustering Coefficient:", avg_clustering_coefficient)

# 6. Degree Distribution
degree_distribution = dict(g_subset.degree())
print("Degree Distribution:", degree_distribution)

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
