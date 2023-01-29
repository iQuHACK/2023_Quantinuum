import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import networkx.algorithms.isomorphism.vf2userfunc as vf2


def subgraphInduce(G, edge, depth, rename=False):
    # return: subgraph induced by edge
    current = set([edge[0], edge[1]])
    edges = set([edge])
    for i in range(depth):
        next = set()
        for node in current:
            next.update(G.neighbors(node))
            edges.update(G.edges(node))
        current.update(next)
    if rename:
        current = {x: i for i, x in enumerate(list(current))}
        edges = [(current[edge[0]], current[edge[1]]) for edge in edges]
    return nx.Graph(list(edges))


# adj = list(G.neighbors(0))
# print(adj[0])
# print(subgraphInduce(G, (0, adj[0]), 1).edges())
# print(subgraphInduce(G, (0, adj[0]), 1, True).edges())

'''
for i in range(40):
    for t in range(20, 30, 2):
        G = nx.random_regular_graph(3, t)
        for edge in G.edges():
            subgraph = subgraphInduce(G, edge, 2)
            seen = False
            # for k, (i, j) in enumerate(res):
            #     if nx.is_isomorphic(subgraph, i):
            #         seen = True
            #         res[k][1] += 1
            #         break
            for i in res:
                if nx.is_isomorphic(subgraph, i):
                    seen = True
                    break
            if not seen:
                #print(len(res))
                #res.append([subgraph, 1])
                res.append(subgraph)'''


def gimme_subgraphs():
    res = []

    for t in range(20, 100, 2):
        G = nx.random_regular_graph(3, t)
        for edge in G.edges():
            subgraph = subgraphInduce(G, edge, 2)
            seen = False
            for i in res:
                if nx.is_isomorphic(subgraph, i):
                    seen = True
                    # res[i][1] += 1
                    break
            if not seen:
                # print(len(res))
                # res.append([subgraph, 1])
                res.append(subgraph)
    print("Generated Subgraphs len = ", len(res))
    return res


# res = sorted(res, key=lambda x: x[1], reverse=True)
# for i in range(100):
#    print(res[i][1])
# nx.draw(G)
# plt.show()
