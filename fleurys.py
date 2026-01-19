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

# Check if edge u-v is a valid next edge to traverse
def isValidNextEdge(u, v, adj, totalV):
    if len(adj[u]) == 1:
        return True

    visited = [False] * totalV
    count1 = 0
    dfsCount(u, adj, visited)
    count1 = sum(visited)

    removeEdge(adj, u, v)

    visited = [False] * totalV
    count2 = 0
    dfsCount(u, adj, visited)
    count2 = sum(visited)

    adj[u].append(v)
    adj[v].append(u)

    return count1 == count2

# Recursively collect the Eulerian 
# path/circuit starting from u
def getEulerUtil(u, adj, edges, v):
    for i in range(len(adj[u])):
        next = adj[u][i]
        if isValidNextEdge(u, next, adj, v):
            edges.append([u, next])
            removeEdge(adj, u, next)
            getEulerUtil(next, adj, edges, v)
            break

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