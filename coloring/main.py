from Graph import Graph
from chromaticPolynomial import ChromaticPolynomial

# Input Format:
# Programmatic Graph Construction:
# g.addVertex(label) for each vertex
# g.addEdge(u, v) for each edge

def main():
    # Create a new Graph
    g = Graph()

    vertices = ["a", "b", "c", "d", "e"]
    for v in vertices:
        g.addVertex(v)

    # Add edges
    g.addEdge("a", "b")
    g.addEdge("b", "c")
    g.addEdge("c", "d")
    g.addEdge("d", "e")
    g.addEdge("e", "a")
    g.addEdge("a", "d")
    g.addEdge("b", "d")

    print(f"Graph created with {g.current_vertices} vertices and {g.current_edges} edges.")

    # Initialize ChromaticPolynomial
    cp = ChromaticPolynomial(g)

    # Calculate the polynomial
    print("Calculating chromatic polynomial...")
    poly = cp.calculatePolynomial()
    print(f"Calculated Polynomial (Unsimplified): {poly}")

    # Simplify the polynomial
    try:
        simplified = cp.simplify(poly, "z")
        print(f"Simplified Polynomial: {simplified}")
    except Exception as e:
        print(f"Could not simplify polynomial (ensure sympy is installed): {e}")

if __name__ == "__main__":
    main()
