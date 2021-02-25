import sys


class Graph():

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        print(f' Edge    Weight')
        print('---------------')
        for i in range(1, self.vertices):
            print(f'{parent[i]} - {i}      {self.graph[i][parent[i]]}')

    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.vertices):
            if key[v] < min and mstSet[v] is False:
                min = key[v]
                min_index = v
        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.vertices
        parent = [None] * self.vertices
        key[0] = 0
        mstSet = [False] * self.vertices

        parent[0] = -1

        for cout in range(self.vertices):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.vertices):
                if self.graph[u][v] > 0 and mstSet[v] is False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


g = Graph(5)
g.graph = [[1, 2, 3, 4, 5],
           [2, 3, 4, 5, 6],
           [3, 4, 5, 6, 7],
           [4, 5, 6, 7, 8],
           [5, 6, 7, 8, 9]]

g.primMST()
