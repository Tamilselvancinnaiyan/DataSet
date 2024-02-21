import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")

G.add_edge("A","C")
G.add_edge("B","C")
G.add_edge("B","D")
G.add_edge("c","D")
G.add_edge("D","E")

nx.draw(G, with_labels=True, node_color="red", node_size=3000)
plt.margins(0.2)
plt.show()
