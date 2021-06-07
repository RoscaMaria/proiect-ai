
from math import sqrt

import numpy as np

def routeDistance4(puncte, n):
    distante = initMatrix(puncte)
    listaTabu = [0]*len(puncte)
    orasOrigine = n
    orasDestinatie = 0
    listaTabu[n] = 1
    ok = 0
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
    while(ok == 0):
       # orasDestinatie = int(np.random.uniform(1, len(puncte)))
        orasDestinatie = int(np.random.uniform(1, 4))
        if(listaTabu[orasDestinatie] == 0):
            ok = 1
        else:
            #orasDestinatie = np.random.uniform(1, len(puncte))
            orasDestinatie = int(np.random.uniform(1, 4))
    a = distante[orasOrigine][orasDestinatie]
    b = matrice[4][1]+matrice[1][3]
    sum = 0
    print("sumaInit", sum)
    oras = 0
    ok = 0
    print("oras dest", orasDestinatie)
    print("oras origine", orasOrigine)
    i = 1
    tabulist2 = [0]*5
    while(ok == 0):
        print("a intrat in ")
        if(matrice[orasOrigine][i] != 0 and tabulist2[orasOrigine] == 0):
            tabulist2[i] = 1
            sum = sum + matrice[orasOrigine][i]
            print("a trecut prin", orasOrigine, i)
            print("s a adaugat", matrice[orasOrigine][i])
            orasOrigine = i
            i = 1
            print("s a schimbat in ", orasOrigine, i)
        i = i+1
        tabulist2.copy()
        print("oras", i)
        print(tabulist2)
        if(i == orasDestinatie):
            tabulist2[orasOrigine] = 1
            sum = sum + matrice[orasOrigine][i]
            print("a trecut prin", orasOrigine, i)
            print("s a adaugat", matrice[orasOrigine][i])
            ok = 1

        print("suma", sum)
    return sum, listaTabu

def distantaRute(puncte, n):
    matrice = matrice1()
    for i in range(1, 5):
        h = 1

def sumOfRoutes(puncte, n):
    ok = 0
    sum2 = 1
    sum, listaTabu = routeDistance4(puncte, n)
    print("suma din sumOfRoutes", sum)
    print("lista tabu din sumOfRoutes",listaTabu)

    orasOrigine = 1
    orasDestinatie = int(np.random.uniform(1, 4))
    i = 1
    """
    while(i <= len(listaTabu)):
        print("a intrat in whileul din sum of routes")
        while(ok == 0):
            if(listaTabu[orasDestinatie] == 0):
                listaTabu[orasDestinatie] = 1
                ok = 1
            else:
                orasDestinatie = int(np.random.uniform(1, 4))
                listaTabu[orasDestinatie] = 1
        print("sum2", sum2)
        sum2 = float(sum2) + float(sum[0])
        print("sum2",sum2)
        sum = routeDistance(puncte, n)
        print("suma ruta", sum[0])"""

def matrice1():
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
def ex(n):
    matrice = matrice1()
    orasOrigine = n
    orasDestinatie = 0
    for i in range(1, 4):
        if(i != orasOrigine):
            orasDestinatie = i




def routeDistance(puncte, n):
    distante = initMatrix(puncte)
   # listaTabu = [0]*len(puncte)
    listaTabu = [0]*10
    orasOrigine = n
    orasDestinatie = 0
    listaTabu[n] = 1
    ok = 0
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
    while(ok == 0):
       # orasDestinatie = int(np.random.uniform(1, len(puncte)))
        orasDestinatie = int(np.random.uniform(1, 4))
        if(listaTabu[orasDestinatie] == 0):
            ok = 1
            listaTabu[orasDestinatie] = 1
        else:
            #orasDestinatie = np.random.uniform(1, len(puncte))
            orasDestinatie = int(np.random.uniform(1, 4))
            listaTabu[orasDestinatie] = 1
        print("lista tabu", listaTabu)

    sum = 0
    print("sumaInit", sum)
    oras = 0
    ok = 0
    print("oras dest", orasDestinatie)
    print("oras origine", orasOrigine)
    i = 0
    tabulist2 = [0]*7
    while(ok == 0):
        i = i + 1
        print("indicele i", i)

        print("a intrat in ")
        print("matrice", matrice[orasOrigine][i])
        print("test matrice",matrice[4][4])
        print("tabuList in while", tabulist2[orasOrigine])
        k = 0
        while(k == 0):

            if(matrice[orasOrigine][i] != 0 and tabulist2[orasOrigine] == 0):

                tabulist2[i] = 1
                sum = sum + matrice[orasOrigine][i]
                print("a trecut prin", orasOrigine, i)
                print("s a adaugat", matrice[orasOrigine][i])
                orasOrigine = i
                i = 1
                print("s a schimbat in ", orasOrigine, i)
                k = 1
            else:
                i = i+1

        tabulist2.copy()
        print("oras", i)
        print(tabulist2)
        if(i == orasDestinatie):
            tabulist2[orasOrigine] = 1
            sum = sum + matrice[orasOrigine][i]
            print("a trecut prin", orasOrigine, i)
            print("s a adaugat", matrice[orasOrigine][i])
            ok = 1

        print("suma", sum)
    return sum, listaTabu



def routeDistance1(puncte, n):
    distante = initMatrix(puncte)
    listaTabu = [0]*len(puncte)
    orasOrigine = n
    orasDestinatie = 0
    listaTabu[n] = 1
    ok = 0
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

   # orasDestinatie = int(np.random.uniform(1, len(puncte)))
    for k in range(1, 5):
        if(orasOrigine != k):
            orasDestinatie = k
            sum = 0
            print("oras destinatie", orasDestinatie)
            print("sumaInit", sum)
            ok = 0
            print("oras dest", orasDestinatie)
            print("oras origine", orasOrigine)
            oras = 1
            tabulist2 = [0]*len(puncte)
            print("tabulist",tabulist2)
            while(ok == 0):
                print("a intrat in ", orasOrigine)
                print("oras in while", oras)
                print("orasDestinatie", orasDestinatie)
                print("matrice", matrice[orasOrigine][oras])
                print("tabu", tabulist2[orasOrigine] )
                if(matrice[orasOrigine][oras] != 0 and tabulist2[orasOrigine] == 0):
                    tabulist2[oras] = 1
                    sum = sum + matrice[orasOrigine][oras]
                    print("a trecut prin", orasOrigine, oras)
                    print("s a adaugat", matrice[orasOrigine][oras])
                    orasOrigine = oras
                    oras = 1
                    print("s a schimbat in ", orasOrigine, oras)
                oras = oras+1
                tabulist2.copy()
                print("oras", oras)
                print(tabulist2)

                if(oras == orasDestinatie):
                    print("intra in if oras = orasDest")
                    tabulist2[orasOrigine] = 1
                    sum = sum + matrice[orasOrigine][oras]
                    print("a trecut prin", orasOrigine, oras)
                    print("s a adaugat", matrice[orasOrigine][oras])
                    ok = 1

            print("suma", sum)
    return sum

def euclideanDistance(a,b):
    return sqrt((b[0]-a[0])*(b[0]-a[0])+(b[1]-a[1])*(b[1]-a[1]))

def readData(filename):
    puncte=[[-1,-1]]
    f = open(filename, "r")
    for x in f:
        print("x:", x)
        data=x.split(" ")
        print(data)
        print(data[1])
        puncte.append([float(data[0]),float(data[1].strip())])
        print(puncte)
    return puncte


def initMatrix(puncte):
    n=len(puncte)
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(1,len(puncte)):
        for j in range(1,len(puncte)):
            matrix[i][j]=euclideanDistance(puncte[i],puncte[j])
            print(i, j, matrix[i][j])
    return matrix
