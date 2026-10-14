from script_5 import recs
import plotly.graph_objects as go

fig = go.Figure(
            go.Sankey(
                    arrangement='snap',
                    node=dict(
                        label=['ArrivalNode', 'ColdFood', 'HotFood', 'Till', 'Exit'],
                        pad=10
                        ),
                    link=dict(
                        arrowlen=15,
                        source=recs.node,
                        target=recs.destination,
                        value=recs.flow
                        )
                )
        )
