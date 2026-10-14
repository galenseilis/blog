from script_6 import fig
fig.layout.paper_bgcolor = 'rgba(0.5,0.5,0.5,0.5)'
fig.layout.plot_bgcolor = 'rgba(0.5,0.5,0.5,0.5)'

print(fig.to_html(full_html=False, include_plotlyjs='cdn'))
