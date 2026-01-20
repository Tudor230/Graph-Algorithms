import heapq

# Input Format:
# adj = Adjacency Dictionary where keys are vertex labels (1-based)
#       and values are lists of neighbors.
# Example: adj = { 1: [5, 7, 3], 2: [4], ... }

def tree_to_prufer(adj):
    n = len(adj)
    degree = [0] * (n + 1)
    
    # Calculate degrees
    for u in adj:
        degree[u] = len(adj[u])
        
    # Find all initial leaves (degree 1)
    leaves = [i for i in range(1, n + 1) if degree[i] == 1]
    # Use a min-heap or sort to easily get the smallest leaf

    heapq.heapify(leaves)
    
    prufer_sequence = []
    
    # We remove vertices until only 2 left.
    processed_count = 0
    while processed_count < n - 2:
        # Get smallest leaf
        u = heapq.heappop(leaves)
        
        # Find its neighbor v
        neighbor = -1
        for v in adj[u]:
            if degree[v] > 0: # valid neighbor in remaining tree
                neighbor = v
                break
        
        if neighbor == -1:
            # Should not happen in a valid tree with > 2 nodes
            break
            
        # Add neighbor to sequence
        prufer_sequence.append(neighbor)
        
        # "Remove" u
        degree[u] -= 1 # u becomes 0 (removed)
        
        # Decrement degree of neighbor
        degree[neighbor] -= 1
        
        # If neighbor becomes a leaf and is not removed, add to heap
        if degree[neighbor] == 1:
            heapq.heappush(leaves, neighbor)
            
        processed_count += 1
        
    return prufer_sequence

if __name__ == "__main__":
    adj = {
        1: [5,7,3],
        2: [4],
        3: [4,6,1],
        4: [2,3],
        5: [1],
        6: [3],
        7: [1],
    }
    

    print("Tree Edges:")
    for u in adj:
        for v in adj[u]:
            if u < v:
                print(f"({u}, {v})")

    seq = tree_to_prufer(adj)
    print("\nPrufer Sequence:", seq)
