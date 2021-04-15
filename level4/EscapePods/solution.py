import collections

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.row = len(graph)

    def extend_graph(self, source, sink):
        super_source = [0] * (len(self.graph[0])+2)
        super_sink = [0] * (len(self.graph[0])+2)
        for r in self.graph:
            r.insert(0,0)
            r.append(0)

        for s in source:
            super_source[s+1] = float('Inf')
        for t in sink:
            self.graph[t][-1] = float('Inf')

        self.graph.insert(0, super_source)
        self.graph.append(super_sink)
        self.row = len(self.graph)

    def bfs(self, s, t, parent):
        visited = [False] * self.row
        queue = collections.deque()
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.popleft()
            for ind, val in enumerate(self.graph[u]):
                if (visited[ind] == False) and (val > 0):
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return visited[t]

    def edmonds_karp(self, source, sink):
        parent = [-1] * self.row
        max_flow = 0
        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow

def solution(entrances, exits, path):
    g = Graph(path)
    g.extend_graph(entrances, exits)
    return g.edmonds_karp(0, (len(g.graph)-1))