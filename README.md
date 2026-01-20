# Graph Theory Algorithms (GTC)

This repository contains Python implementations of various fundamental graph theory algorithms. These scripts cover shortest paths, minimum spanning trees, Eulerian circuits, network flow, and tree encodings.

## Algorithms and Files

### Shortest Path Algorithms
* **Dijkstra's Algorithm** (`dijkstras.py`): Finds the shortest path from a single source vertex to all other vertices in a graph with non-negative edge weights.
* **Floyd-Warshall Algorithm** (`warshall.py`): A dynamic programming algorithm for finding shortest paths between all pairs of vertices in a weighted graph.

### Minimum Spanning Tree (MST)
* **Kruskal's Algorithm** (`kruskall.py`): Finds the Minimum Spanning Tree of a connected, undirected graph by sorting edges by weight and adding them if they don't form a cycle.

### Eulerian Paths and Circuits
* **Fleury's Algorithm** (`fleurys.py`): algorithm to find an Eulerian path or circuit by traversing edges and avoiding bridges unless no other option exists.
* **Hierholzer's Algorithm** (`heirzolers.py`): An efficient algorithm to find an Eulerian circuit in a graph that is known to have one (all vertices have even degree).

### Network Flow
* **Ford-Fulkerson Algorithm** (`ford.py`): Computes the maximum flow in a flow network from a source to a sink. This implementation utilizes BFS (Breadth-First Search) for finding augmenting paths.

### Trees and Sequences
* **Tree to Prüfer Sequence** (`tree_to_prufer.py`): Converts a labeled tree into a Prüfer sequence, which is a unique sequence associated with the tree.
* **Prüfer Sequence to Tree** (`prufer.py`): Reconstructs a labeled tree from a valid Prüfer sequence.

### Graph Coloring
* **Chromatic Polynomial** (`coloring/`): Contains classes and logic to compute the chromatic polynomial of a graph.
  * `coloring/chromaticPolynomial.py`: Core logic for calculating the polynomial using the deletion-contraction principle.
  * `coloring/Graph.py`: Graph data structure helper.
  * `coloring/main.py`: Example usage script.

## Usage

Each script is generally self-contained (except for the `coloring` folder contents). You can look at the main execution block or test function within each file to understand how to input your graph data.

Example for running a script:
```bash
python dijkstras.py
```
