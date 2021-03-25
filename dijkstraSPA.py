import sys


class Graph():

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print('Vertex     Distance from Source')
        for node in range(self.vertices):
            print(f' {node}    \t\t {dist[node]}')

    def minDistance(self, dist, sptSet):
        min = sys.maxsize

        for v in range(self.vertices):
            if dist[v] < min and sptSet[v] is False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):

        dist = [sys.maxsize] * self.vertices
        dist[src] = 0
        sptSet = [False] * self.vertices

        for cout in range(self.vertices):

            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.vertices):
                if self.graph[u][v] > 0 and sptSet[v] is False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 9, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 4, 0, 0, 0],
           [0, 0, 0, 9, 0, 1, 0, 0, 0],
           [0, 0, 4, 4, 1, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 1, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]

g.dijkstra(0)
