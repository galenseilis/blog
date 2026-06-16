import random
import networkx as nx


def random_dag(num_nodes: int, p: float) -> nx.DiGraph:
    """
    Generates a random directed acyclic graph (DAG) by sampling random edges with probability p
    and removing cycles if any are formed.

    Args:
        num_nodes (int): The number of nodes in the graph.
        p (float): Probability of creating a directed edge between any pair of nodes.

    Returns:
        nx.DiGraph: A networkx directed acyclic graph.
    """
    # Step 1: Create an empty directed graph
    dag = nx.DiGraph()

    # Step 2: Add nodes to the graph
    dag.add_nodes_from(range(num_nodes))

    # Step 3: Randomly add directed edges between nodes with probability p
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):  # Ensure no self-loops, i != j
            if random.random() < p:
                dag.add_edge(i, j)
            if random.random() < p:
                dag.add_edge(j, i)

    # Step 4: Remove cycles if any exist
    while not nx.is_directed_acyclic_graph(dag):
        try:
            # Find a cycle (if one exists)
            cycle = nx.find_cycle(dag, orientation="original")
            # Remove a random edge from the cycle to break it
            edge_to_remove = random.choice(cycle)
            dag.remove_edge(*edge_to_remove[:2])
        except nx.exception.NetworkXNoCycle:
            break  # No more cycles, exit the loop

    return dag


if __name__ == "__main__":
    # Generate a random DAG with 5 nodes and a probability p=0.3 for each directed edge
    dag = random_dag(num_nodes=5, p=0.3)

    # Print the edges of the resulting DAG
    print("Edges of the generated DAG:")
    print(list(dag.edges))
