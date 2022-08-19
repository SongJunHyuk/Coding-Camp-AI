def TPL(Matrix):
    total = 0
    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            total += Matrix[i][j]

    return total

def APL(Matrix, TPL):
    return TPL/(len(Matrix)**2 - len(Matrix))

def PLD(Matrix, APL):
    Nr = 0 
    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if Matrix[i][j] == 1:
                Nr += Matrix[i][j]
    return APL/(Nr//2)

class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])
            
    def minDistance(self, dist, sptSet):
 
        min = 1e7

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    def dijkstra(self, src):
 
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            u = self.minDistance(dist, sptSet)
 
            sptSet[u] = True
 
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        return dist

relMatrix = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
[0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
[0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
[0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
[0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]

def sp():
    g = Graph(len(relMatrix))
    g.graph = relMatrix

    result = []
    for i in range(len(relMatrix)):
        result.append(g.dijkstra(i))

    print(*result, sep="\n")

    t = TPL(result)
    a = APL(result, t)
    p = PLD(result, a) 

    print("\nTPL:", t)
    print("APL:", a)
    print("PLD:", p)