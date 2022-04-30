import networkx as nx
import matplotlib.pyplot as plt 



#G = nx.gnp_random_graph(10,5)
G = nx.barabasi_albert_graph(10,5)

nx.draw(G)
plt.plot()
plt.show()