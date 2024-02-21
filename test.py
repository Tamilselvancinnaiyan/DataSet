import networkx as nx
import matplotlib.pyplot as plt

# Load a smaller subset of the graph for demonstration purposes
g = nx.read_edgelist('facebook_combined.txt', create_using=nx.Graph(), nodetype=int)
g_subset = g.subgraph(list(g.nodes())[:4000])

print("Number of nodes:", g_subset.number_of_nodes())
print("Number of edges:", g_subset.number_of_edges())

# Average degree calculation
avg_degree = sum(dict(g_subset.degree()).values()) / g_subset.number_of_nodes()
print("Average Degree:", avg_degree)

#  timeout
timeout = 60
sp = nx.random_layout(g_subset, seed=42)

plt.axis('off')
nx.draw_networkx(g_subset, pos=sp, with_labels=False, node_size=35)
plt.show()
