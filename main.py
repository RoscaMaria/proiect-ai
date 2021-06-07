

from functions import readData, initMatrix, routeDistance1, routeDistance, sumOfRoutes, matrice1, routeDistance4
from incercare2 import matrixToGraph, find_all_paths, depthFirst


def main():
    puncte = readData("eil101.txt")
    matrice = initMatrix(puncte)
    for i in range(len(puncte)):
        for j in range(len(puncte)):
            print(matrice[i][j], end=" ")
        print()

    #routeDistance4(puncte, 4)
    #sumOfRoutes(puncte, 4)
    #matrice1()
    matrixToGraph()
    graph = matrixToGraph()
    visitedList = [[]]
    visited = [0]*10
    currentVertex = 1
    #depthFirst(graph, currentVertex, visited)
    #find_all_paths(1, 3, path=[])
main()