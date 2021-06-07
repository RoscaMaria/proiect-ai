from collections import defaultdict
from pprint import pprint

l =[[  0.,  15.,   0.,   7.,  10.,   0.],
    [ 15.,   0.,   9.,  11.,   0.,   9.],
    [  0.,   9.,   0.,   0.,  12.,   7.],
    [  7.,  11.,   0.,   0.,   8.,  14.],
    [ 10.,   0.,  12.,   8.,   0.,   8.],
    [  0.,   9.,   7.,  14.,   8.,   0.]]
matrice = [[0 for i in range(6)] for j in range(6)]
matrice[1][1] = 0
matrice[1][2] = 2
matrice[1][3] = 5
matrice[1][4] = 3
matrice[2][1] = 2
matrice[2][2] = 0
matrice[2][3] = 1
matrice[2][4] = 0
matrice[3][1] = 5
matrice[3][2] = 1
matrice[3][3] = 0
matrice[3][4] = 3
matrice[4][1] = 3
matrice[4][2] = 0
matrice[4][3] = 3
matrice[4][4] = 0
for i in range(5):
    for j in range(5):
        print(matrice[i][j], end=" ")
    print()

graph = defaultdict(list)
edges = set()

for i, v in enumerate(l, 1):
    for j, u in enumerate(v, 1):
        if u != 0 and frozenset([i, j]) not in edges:
            edges.add(frozenset([i, j]))
            graph[i].append({j: u})
print("graf",graph[1][2])

pprint(graph)

visitedList = [[]]

def depthFirst(graph, currentVertex, visited):
    visited.append(currentVertex)
    for vertex in graph[currentVertex]:
        if vertex not in visited:
            depthFirst(graph, vertex, visited.copy())
    visitedList.append(visited)

print(depthFirst(graph, 0, []))