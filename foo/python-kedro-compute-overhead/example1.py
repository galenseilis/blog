import networkx as nx
from kedro.pipeline import node, Pipeline
from typing import Callable

def construct_kedro_pipeline(func: Callable, dag: nx.DiGraph) -> Pipeline:
    """
    Constructs a Kedro pipeline from a networkx DAG where each node in the graph
    is a Kedro node using the provided function 'func'.
    
    Args:
        func (Callable): A function to apply to each node.
        dag (nx.DiGraph): A directed acyclic graph (DAG) represented as a networkx graph.
    
    Returns:
        Pipeline: A Kedro pipeline constructed based on the DAG structure.
    """
    # Step 1: Check if the graph is a valid DAG
    if not nx.is_directed_acyclic_graph(dag):
        raise ValueError("The provided graph is not a valid Directed Acyclic Graph (DAG).")
    
    # Step 2: Topologically sort the nodes to ensure proper execution order
    topological_order = list(nx.topological_sort(dag))
    
    # Step 3: Create Kedro nodes based on the DAG structure
    kedro_nodes = []
    
    for node_name in topological_order:
        # Get inputs: all predecessors of the current node
        input_edges = list(dag.predecessors(node_name))
        # Get outputs: the current node will output its own name as its output
        output_edges = [node_name]
        
        # Create a Kedro node with the function 'func' for this node
        if input_edges:
            kedro_node = node(
                func=func,         # The function to run at this node
                inputs=input_edges,  # Inputs are the in-edges of the current node
                outputs=output_edges # Outputs are the out-edges (represented as the node itself)
            )
        
            # Add this node to the list of Kedro nodes
            kedro_nodes.append(kedro_node)
    
    # Step 4: Create a Kedro pipeline with the constructed nodes
    pipeline = Pipeline(kedro_nodes)
    
    return pipeline

if __name__ == '__main__':
    # Define the function to be applied at each Kedro node
    def example_func(*args):
        return sum(args)

    # Create a DAG using networkx
    dag = nx.DiGraph()
    dag.add_edges_from([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")])

    # Construct a Kedro pipeline from the DAG
    pipeline = construct_kedro_pipeline(func=example_func, dag=dag)

    # Print the constructed pipeline to inspect its nodes
    print(pipeline)

    help(pipeline)
