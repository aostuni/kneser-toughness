#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools

# In[25]:


n = 10
r = 4

# In[25]:


map = [set(v) for v in itertools.combinations(range(1, n + 1),
                                              r)]  # map between vertices (integers between 0 and |G|-1) and actual sets
v1 = map.index({i for i in range(1, r + 1)})
v2 = map.index({i for i in range(r + 1, 2 * r + 1)})
size = len(map)

G = [[False] * size for i in range(size)]  # Kneser graph as an adjacency matrix
disjoint = [set() for i in range(size)]  # for each vertex v, gives the neighborhood of v
intersecting = [set() for i in range(size)]  # for each vertex v, gives list of vertices not in neighborhood of v

for i in range(size):
    for j in range(i + 1, size):
        if map[i].isdisjoint(map[j]):
            G[i][j] = True
            G[j][i] = True
            disjoint[i].add(j)
            disjoint[j].add(i)
        else:
            intersecting[i].add(j)
            intersecting[j].add(i)

# In[26]:


# print("|V(G)| = " + str(len(G)))
# tot = 0
# for i in range(size):
#     tot += len(disjoint[i])
# print("|E(G)| = " + str(tot // 2))
# print("|d(G)| = " + str(len(disjoint[0])))


# In[4]:


def add_singleton(g):
    """
    Returns set of all possible singleton additions, where the singleton is connected to g.
    g must be a sorted tuple of vertices in G.
    g represents the graph of edges/singletons we're building up.
    """
    a = intersecting[g[0]] & intersecting[g[1]]
    for i in range(2, len(g)):
        a &= intersecting[g[i]]
    return set(tuple(sorted(list(g) + [v])) for v in a)


def add_edge(g):
    """
    Returns set of all possible edge additions, where the edge is not connected to g.
    g must be a sorted tuple of vertices in G.
    g represents the graph of edges/singletons we're building up.
    """
    result = set()
    a = intersecting[g[0]] & intersecting[g[1]]
    for i in range(2, len(g)):
        a &= intersecting[g[i]]
    for v in a:
        for w in a:
            if v < w and G[v][w]:
                result.add(tuple(sorted(list(g) + [v, w])))
    return result


# In[5]:


def min_cutset_size(g):
    """
    Returns "minimum size cutset" must be if Kneser graph is disconnected to g.
    Calculates the union of all neighborhoods of vertices in g.
    g must be a tuple of vertices in G.
    """
    cutset = disjoint[g[0]].union(disjoint[g[1]])
    for i in range(2, len(g)):
        cutset = cutset.union(disjoint[g[i]])
    return len(cutset - set(g))

def min_neighborhood_edges(g):
    """
    Returns number of edges of neighborhood in g.
    g must be a tuple of vertices in G.
    """
    neighborhood = disjoint[g[0]].union(disjoint[g[1]])
    for i in range(2, len(g)):
        neighborhood = neighborhood.union(disjoint[g[i]])
    neighborhood = list(neighborhood - set(g))
    edge_count = 0
    for i in range(len(neighborhood)):
        for j in range(i + 1, len(neighborhood)):
            if G[neighborhood[i]][neighborhood[j]]:
                edge_count += 1
    return edge_count

# In[27]:


edge_1 = {(v1, v2)}  # possibilities with one edge

# min_c = size
# for g in edge_1:
#     min_c = min(min_c, min_cutset_size(g))
# print(min_c)  # should be 2 * C(n-r, r) - 2 - C(n - 2r, r)

min_edges = size
for g in edge_1:
    min_edges = min(min_edges, min_neighborhood_edges(g))
print(min_edges)

# In[28]:


# edge_2 = set() # possibilities with two edges
# for h in add_edge((v1, v2)):
#     # We can assume WLOG that one of the vertices of the second edge contains 1, r + 1.
#     flag = False
#     for v in h:
#         if 1 in map[v] and r + 1 in map[v]:
#             flag = True
#     if flag:
#         edge_2.add(h)
#
# print(len(edge_2))
#
# min_c = size
# min_g = None
# for g in edge_2:
#     c = min_cutset_size(g)
#     if c < min_c:
#         min_c = c
#         min_g = g
# print(min_c)


# In[29]:


# better edge_2 for K(n, 4) where n <= 11 from casework by hand
assert n >= 11 and r == 4

data = {
    (1, 5, 9, 10): [(2, 3, 6, 11), (2, 3, 4, 6), (2, 3, 6, 7)],
    (1, 2, 5, 9): [(3, 6, 10, 11), (3, 4, 6, 10), (3, 6, 7, 10), (3, 4, 6, 7), (3, 6, 7, 8)],
    (1, 2, 3, 5): [(4, 6, 9, 10), (4, 6, 7, 9), (4, 6, 7, 8)],
    (1, 2, 5, 6): [(3, 7, 9, 10), (3, 4, 7, 9), (3, 4, 7, 8)]
}

edge_2 = set()
for a, bl in data.items():
    for b in bl:
        flag = True
        for i in a:
            if i > n:
                flag = False
        for i in b:
            if i > n:
                flag = False
        if flag:
            edge_2.add((v1, v2, map.index(set(a)), map.index(set(b))))

# print(len(edge_2))

# min_c = size
# for g in edge_2:
#     min_c = min(min_c, min_cutset_size(g))
# print(min_c)

min_edges = size
for g in edge_2:
    min_edges = min(min_edges, min_neighborhood_edges(g))
print(min_edges)


# In[19]:


m = 3
a = [set(), edge_1, edge_2]  # possibilities of i <= m edges
for i in range(3, m + 1):
    print(str(i) + " edges")
    s = set()
    for g in a[-1]:
        for h in add_edge(g):
            s.add(h)
    a.append(s)

    print("possibilities: " + str(len(s)))

    # min_c = size
    # for g in s:
    #     min_c = min(min_c, min_cutset_size(g))
    # print("neighborhood: " + str(min_c))

    min_edges = size
    for g in s:
        min_edges = min(min_edges, min_neighborhood_edges(g))
    print("neighborhood edges: " + str(min_edges))

    print()


# In[ ]:


# edge_2_single_1 = set()  # two edges and a singleton
# for g in edge_2:
#     for h in add_singleton(g):
#         edge_2_single_1.add(h)
#
# print(len(edge_2_single_1))
#
# min_c = size
# for g in edge_2_single_1:
#     min_c = min(min_c, min_cutset_size(g))
# print(min_c)
