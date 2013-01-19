import networkx as nx
from random import random, choice

def test():

    def dist((x1, y1), (x2, y2)):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    
    G = nx.Graph()
    # points = [(random(), random()) for _ in xrange(10)]
    points = [(1,1),(2,3),(7,6),(5,4)]
    for p1, p2 in zip(points[:-1], points[1:]):
        G.add_edge(p1, p2, weight=dist(p1, p2))

    for _ in xrange(10):
        p1, p2 = choice(points), choice(points)
        G.add_edge(p1, p2, weight=dist(p1, p2))
    
    # path = nx.astar_path(G, points[0], points[-1], dist)
    # path = nx.dijkstra_path(G, points[0], points[-1], dist)
    path = nx.shortest_path(G, points[0], points[-1], dist)

    print G.nodes()
    print "------"
    print G.edges()
    print "------"
    
    print path

test()
