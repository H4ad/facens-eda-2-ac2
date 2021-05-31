

class FordFulkerson:
    
  def __init__(self, graph):
      self.visitedToken = 1
      self.graph = graph
      
  def run(self, source, sink):
      self.visitedToken = 1

      n = len(self.graph)

      visited = [0]*n

      maxFlow = 0

      while True:
        flow = self.dfs(self.graph.copy(), visited, source, sink, 10**100)

        self.visitedToken += 1

        maxFlow += flow

        if flow == 0:
            return maxFlow

  def dfs(self, graph, visited, node, sink, flow):
      if node == sink:
          return flow

      cap = graph[node]

      visited[node] = self.visitedToken

      for i, capacity in enumerate(cap):
        if visited[i] != self.visitedToken and capacity > 0:
          if capacity < flow:
            flow = capacity

          dfsFlow = self.dfs(graph, visited, i, sink, flow)

          if dfsFlow > 0:
            graph[node][i] -= dfsFlow
            graph[i][node] += dfsFlow

            return dfsFlow

      return 0


graph = [[0, 2, 4, 0],
         [0, 0, 3, 1],
         [0, 0, 0, 5],
         [0, 0, 0, 0]
        ]

ford = FordFulkerson(graph)

graphMaxFlow = ford.run(0, 3)

print('Max Flow: ', graphMaxFlow)