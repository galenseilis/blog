import plotly.express as px

df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')

fig.layout.paper_bgcolor = 'rgba(0,0,0,0)'
fig.layout.plot_bgcolor = 'rgba(0,0,0,0)'
              
fig.to_html(full_html=False, include_plotlyjs='cdn')
