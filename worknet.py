import networkx as nx
import numpy
#import matplotlib.pyplot as plt


G = nx.read_edgelist("/pythonfile/facebook_combined.txt")

N = list(G.nodes())

spll = []

for u in N:
    for v in N:
        if u!= v:
            l = nx.shortest_path__length(G , u , v)
            print("shorrtest path between ", u,"and ", v ,"is of length",l)
            spll.append(l)

min_spl = min(spll)
max_spl = max(spll)
avg_spl = numpy.average(spll)

 

print("Minimum shortest path length :",min_spl)
print("Maximum shortest path length :",max_spl)
print("average shortest path length :",avg_spl)
#  G = nx.Graph()
#  G.add_nodes_from([1,2,3,4])
#  G.add_edges_from([(1,2),(2,1),(2,3),(3,4),(4,1),(3,1)])
#  nx.draw(G , with_labels = True)
#   plt.show()