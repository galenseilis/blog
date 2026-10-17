# chatgpt-plot-covering-diagram documentation

`chatgpt-plot-covering-diagram` packages the plotting function ChatGPT wrote
for the blog post *Asking ChatGPT to Code a Plotting Function for Covering
Diagrams*, along with the graphs used to test it. The function takes a
`networkx.DiGraph`, lays the nodes out one per topological level, marks the
edges it treats as covering relations in red, and returns the Matplotlib axes.

The package is deliberately faithful to the model's output. The post shows
that the function is not a correct covering-diagram plotter in general, so
the code here is useful as a concrete, reproducible record of the attempt
rather than as a ready-made library.

The project follows the [Diátaxis](https://diataxis.fr/) structure:

| I want to... | Read |
| --- | --- |
| learn the package by doing | [Tutorial](tutorials.md) |
| solve a specific problem | [How-to guides](how-to-guides.md) |
| look up functions and classes | [Reference](reference.md) |
| understand the ideas and trade-offs | [Explanation](explanation.md) |

## Contents

- [Tutorial](tutorials.md): draw your first covering diagram and reproduce
  the post's two examples.
- [How-to guides](how-to-guides.md): draw into your own axes, save
  transparent figures, and rerun the examples.
- [Reference](reference.md): the public API and the console script.
- [Explanation](explanation.md): what a covering diagram is meant to show,
  and why the model's function does not produce one.
