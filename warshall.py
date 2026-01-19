# Solves the all-pairs shortest path
# problem using Floyd Warshall algorithm
def floydWarshall(dist):
    V = len(dist)
    INF = 100000000

    # Initialize next_node matrix to reconstruct paths
    # next_node[i][j] stores the next vertex to go to from i to reach j
    next_node = [[None for _ in range(V)] for _ in range(V)]
    for i in range(V):
        for j in range(V):
            # If there is a direct edge (and it's not a self-loop)
            if dist[i][j] != INF and i != j:
                next_node[i][j] = j

    # Add all vertices one by one to
    # the set of intermediate vertices.
    for k in range(V):

        # Pick all vertices as source one by one
        for i in range(V):

            # Pick all vertices as destination
            # for the above picked source
            for j in range(V):
                # If vertex k is on the shortest path from i to j,
                # then update the value of dist[i][j] and next_node[i][j]
                if(dist[i][k] != INF and dist[k][j]!= INF):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_node[i][j] = next_node[i][k]

        # Print the distance matrix after each iteration k
        print(f"\nDistance Matrix after considering vertex {k} as intermediate:")
        for r in range(V):
            for c in range(V):
                if dist[r][c] == INF:
                    print("INF", end="\t")
                else:
                    print(dist[r][c], end="\t")
            print()
    
    return next_node

def constructPath(u, v, next_node):
    # If there's no path
    if next_node[u][v] is None:
        return []
    
    path = [u]
    while u != v:
        u = next_node[u][v]
        path.append(u)
    return path

if __name__ == "__main__":
    
    INF = 100000000;
    # dist = [
    #     [0, 4, INF, 5, INF],
    #     [INF, 0, 1, INF, 6],
    #     [2, INF, 0, 3, INF],
    #     [INF, INF, 1, 0, 2],
    #     [1, INF, INF, 4, 0]
    # ]
    dist = [
        [0,10,2,6],
        [3,0,INF,4],
        [INF,INF,0,3],
        [3,4,1,0]
    ]
    
    # Store the next_node matrix returned by the function
    next_node = floydWarshall(dist)
    
    print("\nShortest Distance Matrix:")
    for i in range(len(dist)):
        for j in range(len(dist)):
            if dist[i][j] == INF:
                print("INF", end="\t")
            else:
                print(dist[i][j], end="\t")
        print()
        
    print("\nShortest Paths:")
    V = len(dist)
    
    # Helper to convert index to letter (0 -> A, 1 -> B, etc.)
    def to_char(n):
        return chr(ord('A') + n)

    for i in range(V):
        for j in range(V):
            if i != j:
                path = constructPath(i, j, next_node)
                print(f"Path {to_char(i)} -> {to_char(j)}: ", end="")
                if path:
                    # Convert path indices to letters
                    path_letters = [to_char(node) for node in path]
                    print(" -> ".join(path_letters), end="")
                    print(f" (Cost: {dist[i][j]})")
                else:
                    print("No path")