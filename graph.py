import networkx as nx
from matplotlib import pyplot as plt


# G = nx.barbell_graph(8,3)
# G1 = nx.star_graph(5)
# g2  = nx.wheel_graph(7)
# b = nx.gnp_random_graph(4,0.5)
# a = nx.path_graph(8)
#G = nx.Graph()
G = nx.DiGraph()
print(G.nodes)
G.add_nodes_from([i for i in range(5) ] )
#print(G.nodes)
G.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,1),(4,1)])
#print(G.edges)
print(list(G.out_edges))

print(list(G.in_edges(4)))
nx.draw(G)
plt.show()

