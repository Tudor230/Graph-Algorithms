from collections import defaultdict

# Input Format:
# graph = Adjacency Matrix (2D List), where graph[u][v] is the capacity of edge u->v
# source = Source vertex (integer index)
# sink = Sink vertex (integer index)

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)


    # Returns true if there is a path from source 's' to sink 't' in
    # residual graph. Also fills parent[] to store the path.
    # Uses BFS to find the shortest augmenting path (Edmonds-Karp implementation).
    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Returns the maximum flow from source to sink in the given graph.
    # It repeatedly finds an augmenting path in the residual graph
    # and adds the path's bottleneck capacity to the max_flow.
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        # Augment the flow while there is a path from source to sink
        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


graph = [[0,23,1,27,0,0,0,0],
         [0,0,0,10,0,0,0,0],
         [0,17,0,0,14,17,0,0],
         [0,0,24,0,0,0,0,0],
         [0,0,0,0,0,24,0,42],
         [0,0,0,0,0,0,0,0],
         [0,0,1,0,0,12,0,0],
         [0,0,0,0,0,0,0,0]]
g = Graph(graph)

source = 0
sink = 5

print("Max Flow: %d " % g.ford_fulkerson(source, sink))