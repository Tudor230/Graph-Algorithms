# Input Format:
# v = Total number of vertices (integer)
# adj = Adjacency List (List of Lists), where adj[u] contains neighbors of u
# Example: adj = [[1, 2], [0, 2], [0, 1, 3], [2]] for a graph with 4 vertices

# Function to remove edge u-v from the graph
def removeEdge(adj, u, v):
    adj[u].remove(v)
    adj[v].remove(u)

# DFS to count reachable vertices from v
def dfsCount(v, adj, visited):
    visited[v] = True

    for neighbor in adj[v]:
        if not visited[neighbor]:
            dfsCount(neighbor, adj, visited)

# Check if edge u-v is a valid next edge to traverse.
# An edge is valid if:
# 1. It is the only adjacent edge for u.
# 2. It is not a bridge (removing it doesn't disconnect the component).
def isValidNextEdge(u, v, adj, totalV):
    # 1. The edge u-v is the only edge remaining for u
    if len(adj[u]) == 1:
        return True

    # 2. Check if the edge is a bridge
    
    # Count vertices reachable from u BEFORE removing the edge
    visited = [False] * totalV
    count1 = 0
    dfsCount(u, adj, visited)
    count1 = sum(visited)

    # Remove the edge to check connectivity
    removeEdge(adj, u, v)

    # Count vertices reachable from u AFTER removing the edge
    visited = [False] * totalV
    count2 = 0
    dfsCount(u, adj, visited)
    count2 = sum(visited)

    # Add the edge back (backtracking)
    adj[u].append(v)
    adj[v].append(u)

    # If count1 is greater than count2, then edge (u, v) is a bridge
    return count1 == count2

# Recursively collect the Eulerian path/circuit starting from u.
# Follows Fleury's Algorithm: always choose non-bridge edges first,
# unless there is no other option.
def getEulerUtil(u, adj, edges, v):
    # Iterate over all adjacent vertices
    for i in range(len(adj[u])):
        next = adj[u][i]
        # Check if edge u-next is valid (not a bridge or is the last option)
        if isValidNextEdge(u, next, adj, v):
            edges.append([u, next])
            removeEdge(adj, u, next) # Burn the bridge (or edge) after crossing
            getEulerUtil(next, adj, edges, v)
            break

# For Eulerian Path: Start at a vertex with odd degree.
# For Eulerian Circuit: Start at any vertex (all degrees are even).
def getEulerTour(v, adj):
    start = 0

    # Find a vertex with odd degree if exists
    for i in range(v):
        if len(adj[i]) % 2 != 0:
            start = i
            break

    edges = []
    getEulerUtil(start, adj, edges, v)
    return edges

if __name__ == "__main__":
    v = 4
    adj = [[1, 2], [0, 2], [0, 1, 3], [2]]

    res = getEulerTour(v, adj)

    for i in range(len(res)):
        print(f"{res[i][0]}-{res[i][1]}", end="")
        if i != len(res) - 1:
            print(", ", end="")