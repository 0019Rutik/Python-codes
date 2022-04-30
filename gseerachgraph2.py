import networkx as nx
import random
from   matplotlib import pyplot as plt

# Create a Directed Graph

def add_edges():
    nodes = list(G.nodes())
    for s in nodes:
        print(s,end="")
        for t in nodes:
            print(t)
            if(s != t):
                r = random.random()
                
                if r < 0.5:
                    G.add_edge(s,t)

    return G

def assign_points(G):
    nodes=list(G.nodes())
    n =[]
    for node in nodes:
        n.append(100)
    return n

def keep_distributing(points,G):
    while(1):
        new_points  = distribute_points(G,points)
        print(new_points)
        points  = new_points
        stop = input("press # to start and any key to break")
        if(stop == '#'):
            break


    return new_points

def distribute_points(G,nodes):
    nodes = list(G.nodes())
    new_points=[]
    for i in range(len(nodes)):
        new_points.append(0)

    for n in  nodes:
        out = list(G.out_edges(n))
        if len(out) == 0:
            new_points[n] =new_points[n]+points[n]
        else:
            share = points[n]/len(out)
            for (src,tgt) in out:
                new_points[tgt] = new_points[tgt]+share
    return new_points




 









G = nx.DiGraph()

G.add_nodes_from([i for i in range(10)])

G = add_edges()

nx.draw(G,with_labels=True)
plt.show()

points =  assign_points(G)

#keep Distributing

final_point = keep_distributing(points,G)