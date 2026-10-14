extern crate petgraph;
use petgraph::graph::Graph;
use petgraph_evcxr::draw_graph;

fn main() {
    let mut g: Graph<&str, &str> = Graph::new();
    let rock = g.add_node("Rock");
    let paper = g.add_node("Paper");
    let scissors = g.add_node("Scissors");

    g.add_edge(rock, scissors, "beats");
    g.add_edge(paper, rock, "beats");
    g.add_edge(scissors, paper, "beats");

    draw_graph(&g);
}
