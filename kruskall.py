from functools import cmp_to_key

# Input Format:
# V = Number of vertices (integer)
# edges = List of edges, where each edge is [u, v, weight]
# Example: edges = [[0, 1, 10], [1, 3, 15], ...]

def comparator(a,b):
    return a[2] - b[2];

# Kruskal's Algorithm to find Minimum Spanning Tree
# 1. Sort all edges in non-decreasing order of their weight
# 2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far.
# 3. If cycle is not formed, include this edge. Else, discard it.
def kruskals_mst(V, edges):

    # Sort all edges
    edges = sorted(edges,key=cmp_to_key(comparator))
    
    # Traverse edges in sorted order
    dsu = DSU(V)
    cost = 0
    count = 0
    mst_edges = []
    
    # Iterate through sorted edges
    for x, y, w in edges:
        
        # Check if the selected edge creates a cycle
        # If u and v are in different sets (find(u) != find(v)), no cycle is formed
        if dsu.find(x) != dsu.find(y):
            dsu.union(x, y)
            cost += w
            mst_edges.append((x, y, w))
            count += 1
            if count == V - 1:
                break
                
    print("Edges in the constructed MST:")
    for u, v, weight in mst_edges:
        print(f"{u} -- {v} == {weight}")
        
    return cost
    
# Disjoint set data structure (Union-Find)
# Keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets.
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    # Find function with path compression
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # Union function by rank/size
    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1


if __name__ == '__main__':
    
    # An edge contains source, destination and weight
    edges = [[0, 1, 10], [1, 3, 15], [2, 3, 4], [2, 0, 6], [0, 3, 5]]
    print("Minimum Cost Spanning Tree:", kruskals_mst(4, edges))